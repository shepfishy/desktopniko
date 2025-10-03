#!/usr/bin/env python3
"""
Desktop Niko - Linux Port
A character named Niko walks around your desktop
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib
import random
import os

# Global list to track all Niko and Pancakes windows
niko_windows = []
pancakes_windows = []

class NikoWindow(Gtk.Window):
    def __init__(self, is_main=True):
        super().__init__()
        
        self.is_main = is_main
        self.can_move = True
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.animation_state = False  # False = stand, True = skip
        self.current_direction = 0  # 0=stand, 1=down, 2=left, 3=up, 4=right
        
        # Smooth movement state
        self.is_moving = False
        self.target_x = 0
        self.target_y = 0
        self.current_x = 0
        self.current_y = 0
        self.move_step = 2  # Keep at 2 pixels per frame for smooth movement
        self.animation_frame_counter = 0
        
        # Drag state
        self.is_being_dragged = False
        
        # Eating state
        self.is_eating = False
        self.eating_timer = 0
        self.eating_duration = 150  # 150 frames = 5 seconds at 30fps
        
        # Window setup
        self.set_decorated(False)
        self.set_app_paintable(True)
        self.set_keep_above(True)
        
        # Make window transparent
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        
        # Load sprites
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.resources_path = os.path.join(self.base_path, "Resources")
        
        self.sprites = {
            'stand_1': self.load_sprite('nikostand_1.png'),
            'stand_2': self.load_sprite('nikostand_2.png'),
            'stand_3': self.load_sprite('nikostand_3.png'),
            'stand_4': self.load_sprite('nikostand_4.png'),
            'skip_1': self.load_sprite('nikoskip_1.png'),
            'skip_2': self.load_sprite('nikoskip_2.png'),
            'skip_3': self.load_sprite('nikoskip_3.png'),
            'skip_4': self.load_sprite('nikoskip_4.png'),
            'eat': self.load_sprite('nikoEat2.png'),
            'pancakes': self.load_sprite('pancakes.png')
        }
        
        # Create image widget
        self.image = Gtk.Image()
        self.current_sprite = self.sprites['stand_1']
        self.image.set_from_pixbuf(self.current_sprite)
        
        # Create event box for mouse events
        self.event_box = Gtk.EventBox()
        self.event_box.add(self.image)
        self.add(self.event_box)
        
        # Set window size based on sprite
        self.set_default_size(49, 72)
        
        # Connect signals
        self.event_box.connect('button-press-event', self.on_button_press)
        self.event_box.connect('motion-notify-event', self.on_motion)
        self.event_box.connect('button-release-event', self.on_button_release)
        self.event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK | 
                                  Gdk.EventMask.BUTTON1_MOTION_MASK |
                                  Gdk.EventMask.BUTTON_RELEASE_MASK)
        
        # Position window randomly on first load
        screen = Gdk.Screen.get_default()
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        self.move(random.randint(100, screen_width - 200), 
                 random.randint(100, screen_height - 200))
        
        # Timer for deciding new direction (4000ms = 4 seconds)
        GLib.timeout_add(4000, self.on_timer)
        
        # Fast timer for smooth movement and animation (33ms = 30fps)
        GLib.timeout_add(33, self.on_animation_frame)
        
        # Add to global list
        niko_windows.append(self)
        
        self.show_all()
    
    def load_sprite(self, filename):
        """Load a sprite image"""
        try:
            path = os.path.join(self.resources_path, filename)
            return GdkPixbuf.Pixbuf.new_from_file(path)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            # Create a placeholder pixbuf
            return GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, True, 8, 49, 72)
    
    def on_button_press(self, widget, event):
        """Handle mouse button press"""
        if event.button == 1:  # Left click - start drag
            self.drag_start_x = event.x_root - self.get_position()[0]
            self.drag_start_y = event.y_root - self.get_position()[1]
            self.is_being_dragged = True
            self.is_moving = False  # Pause movement during drag
        elif event.button == 3:  # Right click - show menu
            self.show_context_menu(event)
        return True
    
    def on_motion(self, widget, event):
        """Handle mouse motion for dragging"""
        if event.state & Gdk.ModifierType.BUTTON1_MASK:
            new_x = int(event.x_root - self.drag_start_x)
            new_y = int(event.y_root - self.drag_start_y)
            self.move(new_x, new_y)
        return True
    
    def on_button_release(self, widget, event):
        """Handle mouse button release"""
        if event.button == 1:  # Left click - end drag
            self.is_being_dragged = False
            self.current_x, self.current_y = self.get_position()
            self.is_moving = True  # Resume movement after drag
        return True
    
    def show_context_menu(self, event):
        """Show right-click context menu"""
        menu = Gtk.Menu()
        
        # Clone
        clone_item = Gtk.MenuItem(label="Clone")
        clone_item.connect('activate', self.on_clone)
        menu.append(clone_item)
        
        # Remove
        remove_item = Gtk.MenuItem(label="Remove")
        remove_item.connect('activate', self.on_remove)
        menu.append(remove_item)
        
        # Remove all
        remove_all_item = Gtk.MenuItem(label="Remove all Niko's")
        remove_all_item.connect('activate', self.on_remove_all)
        menu.append(remove_all_item)
        
        # Stop/Start moving
        toggle_item = Gtk.MenuItem(label="Stop/Start moving")
        toggle_item.connect('activate', self.on_toggle_movement)
        menu.append(toggle_item)
        
        # Stop/Start moving and look back
        toggle_back_item = Gtk.MenuItem(label="Stop/Start moving and look back")
        toggle_back_item.connect('activate', self.on_toggle_movement_back)
        menu.append(toggle_back_item)
        
        # Spawn pancakes
        pancakes_item = Gtk.MenuItem(label="Spawn pancakes")
        pancakes_item.connect('activate', self.on_spawn_pancakes)
        menu.append(pancakes_item)
        
        menu.show_all()
        menu.popup(None, None, None, None, event.button, event.time)
    
    def on_timer(self):
        """Timer callback for random movement direction"""
        if self.can_move and not self.is_being_dragged:
            # Reduce chance of standing still (now only 10% chance instead of 20%)
            num = random.randint(1, 10)
            if num == 1:
                # 10% chance to stand still
                num = 0
            else:
                # 90% chance to move in a direction (1-4)
                num = random.randint(1, 4)
            
            x, y = self.get_position()
            
            # Update current position
            self.current_x = float(x)
            self.current_y = float(y)
            
            # Store current direction for animation
            self.current_direction = num
            
            if num == 0:  # Stand still (only show stand sprite when actually standing)
                self.is_moving = False
                self.animation_state = False
                self.update_sprite()
            elif num == 1:  # Move down
                self.is_moving = True
                self.target_x = self.current_x
                self.target_y = self.current_y + 60  # Increased from 30 to 60
                self.update_sprite()
            elif num == 2:  # Move left
                self.is_moving = True
                self.target_x = self.current_x - 60  # Increased from 30 to 60
                self.target_y = self.current_y
                self.update_sprite()
            elif num == 3:  # Move up
                self.is_moving = True
                self.target_x = self.current_x
                self.target_y = self.current_y - 60  # Increased from 30 to 60
                self.update_sprite()
            elif num == 4:  # Move right
                self.is_moving = True
                self.target_x = self.current_x + 60  # Increased from 30 to 60
                self.target_y = self.current_y
                self.update_sprite()
        
        return True  # Continue timer
    
    def on_animation_frame(self):
        """Fast timer for smooth movement and sprite animation"""
        # Check for nearby pancakes (only when not eating)
        if not self.is_eating:
            self.check_pancakes_proximity()
        
        # Handle eating animation
        if self.is_eating:
            self.eating_timer += 1
            if self.eating_timer >= self.eating_duration:
                # Finish eating, return to normal
                self.is_eating = False
                self.eating_timer = 0
                self.animation_frame_counter = 0  # Reset animation counter
                self.animation_state = False  # Reset to stand state
                self.current_direction = 0  # Reset to forward facing
                self.is_moving = False  # Not moving after eating
                self.update_sprite()
            return True
        
        if self.can_move and self.is_moving and not self.is_being_dragged:
            # Move towards target
            dx = self.target_x - self.current_x
            dy = self.target_y - self.current_y
            
            if abs(dx) > 0 or abs(dy) > 0:
                # Calculate step
                if abs(dx) > self.move_step:
                    step_x = self.move_step if dx > 0 else -self.move_step
                else:
                    step_x = dx
                    
                if abs(dy) > self.move_step:
                    step_y = self.move_step if dy > 0 else -self.move_step
                else:
                    step_y = dy
                
                self.current_x += step_x
                self.current_y += step_y
                self.move(int(self.current_x), int(self.current_y))
                
                # Toggle animation sprite every 5 frames (roughly 4 times per second)
                self.animation_frame_counter += 1
                if self.animation_frame_counter >= 5:
                    self.animation_frame_counter = 0
                    self.animation_state = not self.animation_state
                    self.update_sprite()
            else:
                # Reached target
                self.is_moving = False
        
        return True  # Continue timer
    
    def update_sprite(self):
        """Update the sprite based on current direction and animation state"""
        if self.current_direction == 0:  # Stand/forwards
            sprite_key = 'skip_1' if self.animation_state else 'stand_1'
        elif self.current_direction == 1:  # Down/forwards
            sprite_key = 'skip_1' if self.animation_state else 'stand_1'
        elif self.current_direction == 2:  # Left
            sprite_key = 'skip_2' if self.animation_state else 'stand_2'
        elif self.current_direction == 3:  # Up/backwards
            sprite_key = 'skip_3' if self.animation_state else 'stand_3'
        elif self.current_direction == 4:  # Right
            sprite_key = 'skip_4' if self.animation_state else 'stand_4'
        else:
            sprite_key = 'stand_1'
        
        self.current_sprite = self.sprites[sprite_key]
        self.image.set_from_pixbuf(self.current_sprite)
    
    def check_pancakes_proximity(self):
        """Check if pancakes are near Niko and trigger eating"""
        if self.is_eating:
            return  # Already eating
        
        niko_x, niko_y = self.get_position()
        niko_center_x = niko_x + 25  # Half of 49px width
        niko_center_y = niko_y + 36  # Half of 72px height
        
        for pancake in pancakes_windows[:]:  # Use slice to iterate over copy
            if not pancake.get_visible():
                pancakes_windows.remove(pancake)
                continue
                
            pancake_x, pancake_y = pancake.get_position()
            pancake_center_x = pancake_x + 29  # Half of 58px width
            pancake_center_y = pancake_y + 27  # Half of 54px height
            
            # Calculate distance
            distance = ((niko_center_x - pancake_center_x) ** 2 + 
                       (niko_center_y - pancake_center_y) ** 2) ** 0.5
            
            # If pancakes are within 80 pixels, start eating
            if distance < 80:
                self.start_eating(pancake)
                break
    
    def start_eating(self, pancake):
        """Start eating animation and remove pancakes"""
        self.is_eating = True
        self.is_moving = False
        self.eating_timer = 0
        self.current_sprite = self.sprites['eat']
        self.image.set_from_pixbuf(self.current_sprite)
        
        # Remove the pancakes
        pancake.destroy()
        if pancake in pancakes_windows:
            pancakes_windows.remove(pancake)
    
    def on_clone(self, widget):
        """Clone this Niko"""
        NikoWindow(is_main=False)
    
    def on_remove(self, widget):
        """Remove this Niko"""
        if self in niko_windows:
            niko_windows.remove(self)
        self.destroy()
    
    def on_remove_all(self, widget):
        """Remove all Nikos"""
        Gtk.main_quit()
    
    def on_toggle_movement(self, widget):
        """Toggle movement on/off"""
        self.can_move = not self.can_move
        if not self.can_move:
            self.is_moving = False
            self.current_sprite = self.sprites['stand_1']
            self.image.set_from_pixbuf(self.current_sprite)
    
    def on_toggle_movement_back(self, widget):
        """Toggle movement and look back"""
        self.can_move = not self.can_move
        if not self.can_move:
            self.is_moving = False
            self.current_sprite = self.sprites['stand_3']
            self.image.set_from_pixbuf(self.current_sprite)
    
    def on_spawn_pancakes(self, widget):
        """Spawn pancakes window"""
        PancakesWindow()

class PancakesWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.set_decorated(False)
        self.set_app_paintable(True)
        self.set_keep_above(True)
        
        # Make window transparent
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        
        # Load pancakes sprite
        base_path = os.path.dirname(os.path.abspath(__file__))
        resources_path = os.path.join(base_path, "desktopniko", "Resources")
        
        try:
            path = os.path.join(resources_path, "pancakes.png")
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
        except:
            pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, True, 8, 58, 54)
        
        # Create image widget
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        
        # Create event box for mouse events
        event_box = Gtk.EventBox()
        event_box.add(image)
        self.add(event_box)
        
        # Set window size
        self.set_default_size(58, 54)
        
        # Connect signals
        event_box.connect('button-press-event', self.on_button_press)
        event_box.connect('motion-notify-event', self.on_motion)
        event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK | 
                            Gdk.EventMask.BUTTON1_MOTION_MASK)
        
        # Position window randomly
        screen = Gdk.Screen.get_default()
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        self.move(random.randint(100, screen_width - 200), 
                 random.randint(100, screen_height - 200))
        
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Add to global list
        pancakes_windows.append(self)
        
        self.show_all()
    
    def on_button_press(self, widget, event):
        """Handle mouse button press"""
        if event.button == 1:  # Left click - start drag
            self.drag_start_x = event.x_root - self.get_position()[0]
            self.drag_start_y = event.y_root - self.get_position()[1]
        elif event.button == 3:  # Right click - close
            self.destroy()
        return True
    
    def on_motion(self, widget, event):
        """Handle mouse motion for dragging"""
        if event.state & Gdk.ModifierType.BUTTON1_MASK:
            new_x = int(event.x_root - self.drag_start_x)
            new_y = int(event.y_root - self.drag_start_y)
            self.move(new_x, new_y)
        return True

def main():
    win = NikoWindow(is_main=True)
    win.connect('destroy', Gtk.main_quit)
    Gtk.main()

if __name__ == '__main__':
    main()