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
using static System.Net.Mime.MediaTypeNames;

namespace WpfApp4
{
    /// <summary>
    /// Логика взаимодействия для PlayPage.xaml
    /// </summary>
    public partial class PlayPage : Page
    {
        List<Test> questions;
        int start = -1;
        int rights = 0;
        int count;
        
        public PlayPage(List<Test> questions)
        {
            InitializeComponent();
            this.questions = questions;
            this.count = questions.Count;

            Next();
        }

        private void answer_Click(object sender, RoutedEventArgs e)
        {
            switch((sender as Button).Name)
            {
                case "answer1":
                    {
                        if (questions[start].AnswerTrue == Answers.Первый) rights += 1;
                        break;
                    }
                case "answer2":
                    {
                        if (questions[start].AnswerTrue == Answers.Второй) rights += 1;
                        break;
                    }
                case "answer3":
                    {
                        if (questions[start].AnswerTrue == Answers.Третий) rights += 1;
                        break;
                    }
            }


            Next();
        }

        private void Next()
        {
            if(start < count - 1)
            {
                start++;

                Test test = questions[start];
                name.Text = test.Name;
                desc.Text = test.Description;

                answer1.Content = test.AnswerOne;
                answer2.Content = test.AnswerTwo;
                answer3.Content = test.AnswerThree;

                
            }
            else
            {
                answer1.Visibility = Visibility.Collapsed;
                answer2.Visibility = Visibility.Collapsed;
                answer3.Visibility = Visibility.Collapsed;

                name.SetResourceReference(TextBlock.TextProperty, "RightAnswers");
                desc.Text = $"{rights}/{count}";
            }
        }
    }
}
