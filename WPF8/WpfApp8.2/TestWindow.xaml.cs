using Newtonsoft.Json;
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
using System.Xml.Linq;
using ClassLibrary; //--------------------Проект-----------------//
using Path = System.IO.Path;

namespace WpfApp4
{
    /// <summary>
    /// Логика взаимодействия для TestWindow.xaml
    /// </summary>
    public partial class TestWindow : Window
    {
        private List<Test> tests;
        public TestWindow(bool CanChanged)
        {
            InitializeComponent();

            edit.IsEnabled = CanChanged;
            try
            {
                tests = Manager.Deserializer<List<Test>>();
            }
            catch (FileNotFoundException)
            {
                tests = new List<Test>() { };
            }
        }

        private void exit_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = new MainWindow();
            mw.Show();

            Close();
        }

        private void edit_Click(object sender, RoutedEventArgs e)
        {
            PageFrame.Content = new ChangePage(tests);
        }

        private void play_Click(object sender, RoutedEventArgs e)
        {
            if(tests.Count == 0) PageFrame.Content = new EmptyPage();
            else PageFrame.Content = new PlayPage(tests);

        }
    }
    public enum Answers
    {
        Первый,
        Второй,
        Третий
    }

}



public class Test
{
    public string Name { get; set; }
    public string Description { get; set; }
    public string AnswerOne { get; set; }
    public string AnswerTwo { get; set; }
    public string AnswerThree { get; set; }
    public WpfApp4.Answers? AnswerTrue { get; set; }

    public Test(string name, string description, string answerOne, string answerTwo, string answerThree, WpfApp4.Answers answerTrue)
    {
        Name = name;
        Description = description;
        AnswerOne = answerOne;
        AnswerTwo = answerTwo;
        AnswerThree = answerThree;
        AnswerTrue = answerTrue;
    }
    public Test()
    {
        Name = "";
        Description = "";
        AnswerOne = "";
        AnswerTwo = "";
        AnswerThree = "";
        AnswerTrue = null;
    }
}

