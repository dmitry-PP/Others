using Microsoft.Win32;
using Spire.Xls;
using System;
using System.Collections.Generic;
using System.Data;
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
    /// Логика взаимодействия для ExcelWindow.xaml
    /// </summary>
    public partial class ExcelWindow : Window
    {

        string file = null;
        public ExcelWindow(string filepath = null)
        {
            InitializeComponent();
            InitializeEmptyDataTable();

            if(filepath != null)
            {
                file = filepath;
                try
                {
                    Workbook wb = new Workbook();
                    wb.LoadFromFile(filepath);

                    Worksheet sheet_first = wb.Worksheets[0];
                    CellRange locateRange = sheet_first.AllocatedRange;

                    var dataTable = sheet_first.ExportDataTable(locateRange, true);
                    sheet.ItemsSource = dataTable.DefaultView;

                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка при загрузке файла: {ex.Message}");
                }
            }
        }

        private void InitializeEmptyDataTable()
        {
            DataTable dataTable = new DataTable();

            dataTable.Columns.Add("Колонка 1");

            sheet.ItemsSource = dataTable.DefaultView;
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
            saveFileDialog.Filter = "Excel Files|*.xls;*.xlsx;*.xlsm";

            if (saveFileDialog.ShowDialog() == true)
            {
                try
                {
                    var dataTable = sheet.ItemsSource as DataView;
                    if (dataTable == null)
                    {
                        MessageBox.Show("Пусто");
                        return;
                    }

                    Workbook wb = new Workbook();
                    wb.Worksheets.Clear();
                    Worksheet sheet_save = wb.Worksheets.Add("Лист 1");

                    sheet_save.InsertDataView(dataTable, true, 1, 1);
                    wb.SaveToFile(saveFileDialog.FileName, Spire.Xls.FileFormat.Version2016);
                    file = saveFileDialog.FileName;

                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка при сохранении файла: {ex.Message}");
                }
            }
        }


        private void Add(object sender, RoutedEventArgs e)
        {
            string columnName = Column.Text;

            if (!string.IsNullOrEmpty(columnName))
            {

                DataView dataView = sheet.ItemsSource as DataView;

                DataTable dataTable = dataView.Table;


                dataTable.Columns.Add(columnName);


                sheet.ItemsSource = null;
                sheet.ItemsSource = dataTable.DefaultView;


                sheet.UpdateLayout();


                Column.Text = "Введите название колонки";


            }
            else
            {
                MessageBox.Show("Введите название!!!");
            }
        }
    }
}
