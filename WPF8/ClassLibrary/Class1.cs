using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ClassLibrary
{
    public static class Manager
    {
        static private string path = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "Tests.json");

        static public void Serializer<T>(T records)
        {
            string json = JsonConvert.SerializeObject(records);

            File.WriteAllText(path, json);

        }

        static public T Deserializer<T>()
        {
            string json = File.ReadAllText(path);
            T data = JsonConvert.DeserializeObject<T>(json);

            return data;
        }
    }
}
