   M S B A M L   `   `   `  ����B  >WpfApp1, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:WpfApp1WpfApp1  5   	       WpfApp1.ExcelWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   'localclr-namespace:WpfApp1     5   	     � Title$  ExcelWindow��5   	   $	��450��6   $	��800��6*   .��5	      �  � ColumnDefinitions 5
   
   �� 5      $��3* �6   �� 5      $��1* �6    � RowDefinitions 5   
   �� 5      $��40 �6   �� 5      $��* �6   �� 5      $��40 �6   �� 5      $��40 �6   .+�5   
   �� -   5         ��Name$ Column��5   /   $��Center=�6    �� TextWrapping$
 Wrap=�6?   $4��.Введите название колонки��6S   $��Center=�6s   $	��600��6�   $��35��6�   �� 5   
   -   5        $��1��5      $%��Добавить колонку��6!   $��Center=�6<   $	��200��6Y   $��35��6e   $��Center=�6q   6�   &   System.Windows.Controls.DataGrid  5   
   -   5          Name$ sheet��5      $��0,35,0,3q�6"   $��1��64   $��2��6A   �� 5   
   -   5        $(��"Отправить по почте��5      $
��Left=�6.   $	��Top=�6I   $	��800��6a   $��35��6m   $��2��6y   $��2��6�   $��0,2,0,0q�6�   �� 5   
   -   5        $��Сохранить��5      $
��Left=�6%   $��Center=�6@   $	��800��6[   $��35��6g   $��3��6s   $��2��6�   5      5      