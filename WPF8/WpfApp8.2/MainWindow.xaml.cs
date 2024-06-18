using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp4
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private static string KeyWord = "lol";
        private static string lang = "ru";
        public MainWindow()
        {
            InitializeComponent();

        }

        private void play_Click(object sender, RoutedEventArgs e)
        {
            SHowWindow();
        }

        private void change_Click(object sender, RoutedEventArgs e)
        {
            auth.Visibility = Visibility.Visible;

        }

        private void auth_TextChanged(object sender, TextChangedEventArgs e)
        {
            if(auth.Text == KeyWord)
            {
                SHowWindow(true);
            }
        }
        private void SHowWindow(bool CanChanged = false)
        {
            

            TestWindow tw = new TestWindow(CanChanged);
            tw.Show();

            Close();
        }

        private void switch_Click(object sender, RoutedEventArgs e)
        {
            if(switcher.Content.ToString() == "ru")
            {
                switcher.Content = lang = "en";
                App.Language = "English";
            }
            else
            {
                switcher.Content = lang = "ru";
                App.Language = "Russia";
            }
        }
    }
}
