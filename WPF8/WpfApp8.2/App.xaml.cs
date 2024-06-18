using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;


namespace WpfApp4
{
    /// <summary>
    /// Логика взаимодействия для App.xaml
    /// </summary>
    public partial class App : Application
    {

        private static string lang;
        public static string Language { 
            get { return lang; }
            set {
                
                var location = System.Reflection.Assembly.GetExecutingAssembly().Location;
                string path = Path.GetDirectoryName(location);
                string di = new DirectoryInfo(path).Parent.Parent.Parent.FullName;

                Uri uri = new Uri($@"{di}\Language\Themes\{value}.xaml",UriKind.Absolute);
                Console.WriteLine(uri.ToString());

                var dict = new ResourceDictionary { Source = uri };

                Current.Resources.MergedDictionaries.RemoveAt(2);//Так как в MergedDictionaries 3 элемента, два из которых materialdesign
                Current.Resources.MergedDictionaries.Insert(2, dict);
            }
        }
    }
}
