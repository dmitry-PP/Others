   M S B A M L   `   `   `  ����B  >WpfApp1, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:WpfApp1WpfApp1  5   	       WpfApp1.WordWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   'localclr-namespace:WpfApp1     5   	     � Title$  
WordWindow��5   	   $	��450��6   $	��800��6)   .��5	      �  � RowDefinitions 5   
   �� 5      $��40 �6   �� 5      �� 5      $
��Auto �6   .+�5   
   c� $��0,0,0,3q�6   .@�5      �� $	��Cut��6   $	��Cut��6#   �� 5      $
��Copy��6   $
��Copy��6$   �� 5      $��Paste��6   $��Paste��6%   �� 5      �� 5      $
��Undo��6   $
��Undo��6$   �� 5      $
��Redo��6   $
��Redo��6$   �� 5      �� 5      $��
ToggleBold��6   $
��Bold��6*   �� 5      $��ToggleItalic��6   $��Italic��6,   �� 5      $��ToggleUnderline��6   $��	Underline��6/   �� 5      �� 5      $��IncreaseFontSize��6   $��Increase Font Size��60   �� 5      $��DecreaseFontSize��6   $��Decrease Font Size��60   �� 5      �� 5      $��	AlignLeft��6   $��
Align Left��6)   �� 5       $��AlignCenter��6   $��Align Center��6+   �� 5!      $��
AlignRight��6   $��Align Right��6*   �� 5"      $��AlignJustify��6   $��Align Justify��6,   �� 5#      �� 5$      $��IncreaseIndentation��6   $��Increase Indentation��63   �� 5%      $��DecreaseIndentation��6   $��Decrease Indentation��63   5&      �� 5'   
   -   5         ��Name$ content��5'      $	��Top=�6'   $��0,2,0,1q�6F   $��1��6W    � 	Resources 5(       �� 
TargetType �� Property �� Value��%X   'J�       �� 5)      " J�6   .�5*      ��  �@��Margin$ 0q�6/   5+      5,      5-      �� 5.   
   -   5        $(��"Отправить по почте��5.      $
��Left=�6.   $��0,4,0,0q�6I   $	��Top=�6Z   $	��800��6r   $��25��6~   $��2��6�   �� 5/   
   -   5        $��Сохранить��5/      $
��Left=�6%   $��0,29,0,0q�6@   $	��Top=�6R   $	��800��6j   $��25��6v   $��2��6�   50      51      