# Baidu Push

This project is an attempt to push URLs to Baidu for indexing per the instructions in their webmaster tools. A Flask application is used so that users can input a sitemap which is then parsed for URLs and submitted to Baidu via a PUSH request. 

## Installation

    # Open a terminal and clone this repo
    $ git clone repo_location

    # Create virtual environment (example with Anaconda python)
    $ Conda create -n env_name_here python=3.5 -y

    # Activate environment
    $ source activate env_name_here

    # Install requirements
    $ cd path/to/project/directory
    $ pip install -r requirements.txt

## Running Program

    # open a terminal in the project folder & activate environment
    $ source activate env_name_here

    # Start Program
    $ python manage.py

    # Open a browser and go to 127.0.0.1:5000

## How it Works

We crawl a websites XML sitemap to create a Pandas Dataframe of the websites URLs. We then feed this into a script that attaches a site and token (per Baidu's instructions) and submits the URLs in a Push request.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

MIT License

Copyright (c) 2016 Eric Watson & [Kevin Tarvin](http://www.kevintarvin.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
