using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace desktopniko
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public bool canmove = true;
        public const int WM_NCLBUTTONDOWN = 0xA1;
        public const int HT_CAPTION = 0x2;

        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int SendMessage(IntPtr hWnd, int Msg, int wParam, int lParam);
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern bool ReleaseCapture();

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                ReleaseCapture();
                SendMessage(Handle, WM_NCLBUTTONDOWN, HT_CAPTION, 0);
            }
            if (e.Button == MouseButtons.Right)
            {
                this.contextMenuStrip1.Show(this, new Point(e.X, e.Y));
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (canmove == true)
            {
                Random r = new Random();
                int num = r.Next(0, 4);
                if (num == 0)
                {
                    this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikostand_1);
                }
                if (num == 1)
                {
                    this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikoskip_1);
                    this.Top = this.Top + 30;
                }
                if (num == 2)
                {
                    this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikoskip_2);
                    this.Left = this.Left - 30;
                }
                if (num == 3)
                {
                    this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikoskip_3);
                    this.Top = this.Top - 30;
                }
                if (num == 4)
                {
                    this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikoskip_4);
                    this.Left = this.Left + 30;
                }
            }
        }

        private void cloneToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form1 nikoclone = new Form1();
            nikoclone.Show();
        }

        private void removeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void removeAllNikosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            System.Windows.Forms.Application.Exit();
        }

        private void stopMovingToolStripMenuItem_Click(object sender, EventArgs e)
        {
            canmove = !canmove;
            this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikostand_1);
        }

        private void stopStartMovingAndLookBackToolStripMenuItem_Click(object sender, EventArgs e)
        {
            canmove = !canmove;
            this.BackgroundImage = new Bitmap(desktopniko.Properties.Resources.nikostand_3);
        }

        private void spawnPancakesInToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 pancakes = new Form2();
            pancakes.Show();
        }
    }
}
