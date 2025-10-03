# Desktop Niko - Linux Port

A character named Niko walks around your desktop.

Customised it a bunch -> fixed movement speed and animations (because they we're just bricked lmao)

I did this because I wanted a linux for more than just XFCE, so I took this one and changed it up a bit.

## Usage

Run the application:
```bash
python3 desktopniko_linux.py
```

Right-click on Niko to open the control menu for options like cloning, spawning pancakes, and controlling movement.

## Requirements/ Prerequisites

- Python 3
- GTK 3
- PyGObject (gi)

Install dependencies:
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

## Credits

Original Windows version by [@Alexplayrus2](https://github.com/Alexplayrus2/desktopniko) and Niko character from [OneShot](https://store.steampowered.com/app/420530/OneShot/) by Eliza, Michael, and Nightmargin.

### More info

This is almost entirely reprogrammed, leaving in the context menu and fixing up some other stuff.
