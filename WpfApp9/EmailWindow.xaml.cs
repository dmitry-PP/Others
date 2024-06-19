using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Mail;
using System.Net;
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

namespace WpfApp1
{
    /// <summary>
    /// Логика взаимодействия для EmailWindow.xaml
    /// </summary>
    public partial class EmailWindow : Window
    {
        string filePath = string.Empty;
        public EmailWindow(string file)
        {
         
            this.filePath = file;
            InitializeComponent();
        }

        private void Send(object sender, RoutedEventArgs e)
        {
            MailMessage message = new MailMessage(login.Text, to.Text, theme.Text,"Отправлено из приложения");


            if (!string.IsNullOrEmpty(filePath))
            {

                Attachment attachment = new Attachment(filePath);
                message.Attachments.Add(attachment);
            }



            SmtpClient client = null;
            string domen;

            if (login.Text.EndsWith("@mail.ru"))
            {
                domen = "smtp.mail.ru";
            }
            else if (login.Text.EndsWith("@gmail.com"))
            {
                domen = "smtp.gmail.ru";
            }
            else if (login.Text.EndsWith("@rambler.ru"))
            {
                domen = "smtp.rambler.ru";
            }
            else if (login.Text.EndsWith("@yandex.ru"))
            {
                domen = "smtp.yandex.ru";
            }
            else
            {
                MessageBox.Show("Введите правильный домен.");
                return;
            }

            client = new SmtpClient("smtp.yandex.ru", 587)
            {
                Credentials = new NetworkCredential(login.Text, pwd.Password),
                EnableSsl = true
            };

            try
            {
                client.Send(message);
                MessageBox.Show("Письмо успешно отправлено!");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ошибка: " + ex.Message);
            }

            Close();
        }

    }
}
