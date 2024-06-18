using ClassLibrary;
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
    /// Логика взаимодействия для ChangePage.xaml
    /// </summary>
    public partial class ChangePage : Page
    {
        public ChangePage(List<Test> tests)
        {
            InitializeComponent();

            data.ItemsSource = tests;
        }

        private void data_RowEditEnding(object sender, DataGridRowEditEndingEventArgs e)
        {
            

            if (data.SelectedItem == null)
            {
                (sender as DataGrid).RowEditEnding -= data_RowEditEnding;
                (sender as DataGrid).CommitEdit();
                (sender as DataGrid).Items.Refresh();
                (sender as DataGrid).RowEditEnding += data_RowEditEnding;

                Console.WriteLine("Row edit");

                List<Test> lst = new List<Test>() { };
                foreach (var item in data.Items)
                {
                    lst.Add(item as Test);
                }

                Console.WriteLine(lst.Count);

                Manager.Serializer(lst.Take(lst.Count - 1).ToList());
            }

        }

        private void data_AddingNewItem(object sender, AddingNewItemEventArgs e)
        {
            Console.WriteLine("adding");
        }
    }
}
