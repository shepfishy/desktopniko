namespace desktopniko
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.cloneToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.removeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.removeAllNikosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.stopMovingToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.stopStartMovingAndLookBackToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.spawnPancakesInToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 2000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.BackColor = System.Drawing.Color.White;
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cloneToolStripMenuItem,
            this.removeToolStripMenuItem,
            this.removeAllNikosToolStripMenuItem,
            this.stopMovingToolStripMenuItem,
            this.stopStartMovingAndLookBackToolStripMenuItem,
            this.spawnPancakesInToolStripMenuItem});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(249, 158);
            this.contextMenuStrip1.Text = "Niko Control Menu";
            // 
            // cloneToolStripMenuItem
            // 
            this.cloneToolStripMenuItem.Name = "cloneToolStripMenuItem";
            this.cloneToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.cloneToolStripMenuItem.Text = "Clone";
            this.cloneToolStripMenuItem.Click += new System.EventHandler(this.cloneToolStripMenuItem_Click);
            // 
            // removeToolStripMenuItem
            // 
            this.removeToolStripMenuItem.Name = "removeToolStripMenuItem";
            this.removeToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.removeToolStripMenuItem.Text = "Remove";
            this.removeToolStripMenuItem.Click += new System.EventHandler(this.removeToolStripMenuItem_Click);
            // 
            // removeAllNikosToolStripMenuItem
            // 
            this.removeAllNikosToolStripMenuItem.Name = "removeAllNikosToolStripMenuItem";
            this.removeAllNikosToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.removeAllNikosToolStripMenuItem.Text = "Remove all Niko\'s";
            this.removeAllNikosToolStripMenuItem.Click += new System.EventHandler(this.removeAllNikosToolStripMenuItem_Click);
            // 
            // stopMovingToolStripMenuItem
            // 
            this.stopMovingToolStripMenuItem.Name = "stopMovingToolStripMenuItem";
            this.stopMovingToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.stopMovingToolStripMenuItem.Text = "Stop/Start moving";
            this.stopMovingToolStripMenuItem.Click += new System.EventHandler(this.stopMovingToolStripMenuItem_Click);
            // 
            // stopStartMovingAndLookBackToolStripMenuItem
            // 
            this.stopStartMovingAndLookBackToolStripMenuItem.Name = "stopStartMovingAndLookBackToolStripMenuItem";
            this.stopStartMovingAndLookBackToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.stopStartMovingAndLookBackToolStripMenuItem.Text = "Stop/Start moving and look back";
            this.stopStartMovingAndLookBackToolStripMenuItem.Click += new System.EventHandler(this.stopStartMovingAndLookBackToolStripMenuItem_Click);
            // 
            // spawnPancakesInToolStripMenuItem
            // 
            this.spawnPancakesInToolStripMenuItem.Name = "spawnPancakesInToolStripMenuItem";
            this.spawnPancakesInToolStripMenuItem.Size = new System.Drawing.Size(248, 22);
            this.spawnPancakesInToolStripMenuItem.Text = "Spawn pancakes in";
            this.spawnPancakesInToolStripMenuItem.Click += new System.EventHandler(this.spawnPancakesInToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Lime;
            this.BackgroundImage = global::desktopniko.Properties.Resources.nikostand_1;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.ClientSize = new System.Drawing.Size(49, 72);
            this.Cursor = System.Windows.Forms.Cursors.Hand;
            this.DoubleBuffered = true;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Form1";
            this.Text = "Niko";
            this.TopMost = true;
            this.TransparencyKey = System.Drawing.Color.Lime;
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseDown);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem cloneToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem removeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem removeAllNikosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem stopMovingToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem stopStartMovingAndLookBackToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem spawnPancakesInToolStripMenuItem;
    }
}

