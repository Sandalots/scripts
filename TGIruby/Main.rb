require_relative 'tg.rb'
require 'tk'

root = TkRoot.new { title "Hello, World!" }
root.geometry("280x100")
root.title("The Great Intelligence")
root.resizable(0,0)

TkLabel.new(root) do
   text 'The Great Intelligence'
   font TkFont.new('times 15 bold')
   pack { padx 15 ; pady 15; side 'left' }
end
Lbl = TkLabel.new(root) do
   text
   pack { padx 15 ; pady 15; side 'left' }
end
Lbl['text'] = $episodes.keys.sample.capitalize()

root.bind("ButtonRelease-1") {
   Lbl['text'] = $episodes.keys.sample.capitalize()
}

root.bind("ButtonRelease-3") {
   root.destroy()
}
Tk.mainloop