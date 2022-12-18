require 'open-uri'
require 'nokogiri'

# Scrape episode data from the Doctor Who Wiki
def scrape_episode_data
  episodes = []
  doc = Nokogiri::HTML(open("https://tardis.fandom.com/wiki/Doctor_Who_Episodes"))
  doc.css("table.wikitable tr").each do |row|
    cells = row.css("td")
    if cells.length == 7
      title = cells[0].text
      season = cells[1].text.to_i
      episode = cells[2].text.to_i
      date = cells[4].text
      writer = cells[5].text
      director = cells[6].text
      episodes << { title: title, season: season, episode: episode, date: date, writer: writer, director: director }
    end
  end
  episodes
end

# Display the episode data in a table
def display_episode_data(episodes)
  puts "Title | Season | Episode | Airing Date | Writer | Director"
  puts "------|--------|---------|-------------|--------|---------"
  episodes.each do |episode|
    puts "#{episode[:title]} | #{episode[:season]} | #{episode[:episode]} | #{episode[:date]} | #{episode[:writer]} | #{episode[:director]}"
  end
end

# Main program
def main
  episodes = scrape_episode_data
  display_episode_data(episodes)
end

main 
