   M S B A M L   `   `   `  ����B  >WpfApp4, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:WpfApp4WpfApp4  5   	       WpfApp4.MainWindow   5   	   _ [MaterialDesignThemes.Wpf, Version=5.0.0.0, Culture=neutral, PublicKeyToken=df2a72020bd7962aFmaterialDesign1http://materialdesigninxaml.net/winfx/xaml/themes  5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   'localclr-namespace:WpfApp4     5   	     � Title$  
MainWindow��5	   	   $	��450��6   $	��400��6)   .��5
      �  � RowDefinitions 5   
   �� 5      $
��auto �6   �� 5      �� 5      $��50 �6   �� 5      $��80 �6   �� 5      $��50 �6   �� 5      $��50 �6   �� 5      $��50 �6    � ColumnDefinitions 5   
   �� 5      .+�5   
   �� -   5         ��Name$ switcher��5      $��35��6#   $��55��6/   $��ru��6:   $��Right=�6G   $��Center=�6c   $��18(�6~   6�   �� 5   
      Role#���   6   $��Center=�62   $��Center=�6O   $��36(�6j   $��1��6x   �� 5   
   -   5        $
 play��5        Play#���  6   $��2��6@   $��	15,0,15,0q�6M   $��20(�6`   $��60��6�   $��
16,4,16,15q�6�   �� 5   
   -   5        $ change��5       
 Change#���  6!   $��4��6E   $��	15,0,15,0q�6R   $��20(�6e   $��60��6�   $��
16,4,16,15q�6�   �� 5   
   -   5         ��Name$
 auth��5      $��6��6    $y�	Collapsed=�6-   $	��200��6c   $��0,0,0,10q�6o   5      5      