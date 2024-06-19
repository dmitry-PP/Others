using Microsoft.Win32;
using Spire.Doc;
using System;
using System.Collections.Generic;
using System.IO;
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
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Логика взаимодействия для WordWindow.xaml
    /// </summary>
    public partial class WordWindow : Window
    {
        string file = null;
        public WordWindow(string filepath = null)
        {
            InitializeComponent();

            if (filepath != null)
            {
                file = filepath;
                try
                {
                    Document doc = new Document();
                    doc.LoadFromFile(filepath);

                    content.Document.Blocks.Clear();
                    content.Document.Blocks.Add(new Paragraph(new Run(doc.GetText())));
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка при загрузке файла: {ex.Message}");
                }

            }
        }
        private void Send(object sender, RoutedEventArgs e)
        {
            if (file == null)
            {
                MessageBox.Show("Сохраните файл сначала");
                return;                
            }
            EmailWindow window = new EmailWindow(file);
            window.Show();
        }

        private void Save(object sender, RoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Word documents (.docx)|*.docx";
            if (saveFileDialog.ShowDialog() == true)
            {
                string filePath = saveFileDialog.FileName;

                Document doc = new Document();
                doc.AddSection().AddParagraph().AppendText(new TextRange(content.Document.ContentStart, content.Document.ContentEnd).Text);
                doc.SaveToFile(filePath, FileFormat.Docx);

                file = filePath;
            }
        }

    }
}
