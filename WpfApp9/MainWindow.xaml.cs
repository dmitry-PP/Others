using System;
using System.Data;
using System.IO;
using System.Net;
using System.Net.Mail;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using Microsoft.Win32;
using Spire.Doc;
using Spire.Doc.Documents;
using Spire.Xls;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {

        public MainWindow()
        {
            InitializeComponent();
        }

        private void WordCreate(object sender, RoutedEventArgs e)
        {
            WordWindow window = new WordWindow();
            window.Show();
            Close();
        }

        private void ExcelCreate(object sender, RoutedEventArgs e)
        {
            ExcelWindow window = new ExcelWindow();
            window.Show();
            Close();
        }

        private void WordOpen(object sender, RoutedEventArgs e)
        {

            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Word documents (.docx)|*.docx";
            if (openFileDialog.ShowDialog() == true)
            {
                string filePath = openFileDialog.FileName;
                WordWindow window = new WordWindow(filePath);
                window.Show();
                Close();

            }
            
        }

        private void ExcelOpen(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Excel Files|*.xls;*.xlsx;*.xlsm";
            if (openFileDialog.ShowDialog() == true)
            {
                string filePath = openFileDialog.FileName;
                ExcelWindow window = new ExcelWindow(filePath);
                window.Show();
                Close();

            }
        }
    }
}
