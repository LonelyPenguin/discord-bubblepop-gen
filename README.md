This is a simple webpage that facilitates easy generation of "discord bubblewrap," a.k.a. some characters individually enclosed in spoiler markers. Each separate spoiler-tag enclosure is known as a "bubble." Bubbles do not need to be consistent in length.

It has two editors: a basic editor, which is just a single text box, and a grid editor, in which each square in the grid is one bubble.

In the basic editor, bubbles are separated by commas, or by spaces if no commas are detected. Each row can contain any number of bubbles.

In the grid editor, the dimensions of the grid are customisable, and the "autofill" option will prefill the grid with whatever is inputted. These prefills can be overwritten. Empty boxes will still get spoiler markdown tags generated for them, and will look wonky once pasted into Discord. It is up to the user (you) to delete these. Sorry.

Pressing enter or clicking any of the submission buttons will reset the contents of all other sections of the page; be careful.

If you'd like to run this site on your own computer, download the whole folder and all its contents (or clone the repository), install Flask (and Python, of course), and run the command "flask --app logic run" from within the directory.

You can access the web-hosted version at https://discord-bubblewrap.herokuapp.com/.

This is a hobby project and I make no guarantees as to its quality, length of life, etc.

Many thanks to the wonderful people on the Murderbot Diaries 2.0 Discord server, which has a thread dedicated to posting these "bubble wraps" and inspired me to make this little tool for them.
