require_relative 'tg.rb'
require 'tk'

root = TkRoot.new { title "Hello, World!" }
root.geometry("400x400")
root.title("The Great Intelligence")

TkLabel.new(root) do
   text 'The Great Intelligence'
   pack { padx 15 ; pady 15; side 'left' }
end
Lbl = TkLabel.new(root) do
   text
   pack { padx 15 ; pady 15; side 'left' }
end
Lbl['text'] = $episodes.keys.sample

Tk.mainloop