require_relative 'db.rb'
require 'tk'

class Main
    def initialize(list)
        @episodeList = list
    end
    def run()
        puts(@episodeList.keys.sample)
    end
end

s = Main.new($episodes)
s.run