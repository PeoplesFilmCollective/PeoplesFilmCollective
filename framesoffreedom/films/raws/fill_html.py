#!/bin/python

import pandas as pd
import os

csvfile = pd.read_csv('FOF_Film_Data.csv', sep='\t', delimiter=None, on_bad_lines='skip')
csvfile.fillna('', inplace=True)
row_limit, col_limit = csvfile.shape
cwd = os.getcwd()

for i in range(1,row_limit):

  fof_year = str(int(csvfile["FOF"].values[i]))
  directory_path = cwd + '/' + str(fof_year)
  print(directory_path)
  if not os.path.exists(directory_path):
    os.makedirs(directory_path)

  file_name = str(csvfile["MOVIE_NAME"].values[i]).lower().replace(' ', '-')
  img_dir = cwd + '/' + fof_year + '/images/' + file_name
  if not os.path.exists(img_dir):
    os.makedirs(img_dir)
  print(file_name)
  html_file = open(str(cwd + '/' + fof_year + '/' + file_name + '.html'), 'w+')

  file_contents = '''<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <link
        rel="icon"
        type="image/x-icon"
        href="../../../assets/Image/favicon.png"
      />
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/fork-awesome@1.2.0/css/fork-awesome.min.css"
        integrity="sha256-XoaMnoYC5TH6/+ihMEnospgm0J1PM/nioxbOUdnM8HY="
        crossorigin="anonymous"
      />
      <link rel="stylesheet" href="../../assets/CSS/single-film-page.css" />
      <title id="film_name">''' + str(csvfile["MOVIE_NAME"].values[i]) +'''</title>
    </head>
    <body>
      <nav class="navbar">
        <div class="navbar-container container">
          <input type="checkbox" name="" id="checkbox" />
          <div
            class="hamburger-lines"
            onclick='document.getElementById("checkbox").checked = !document.getElementById("checkbox").checked'
          >
            <span class="line line1"></span>
            <span class="line line2"></span>
            <span class="line line3"></span>
          </div>
          <ul class="menu-items">
            <li><a href="../../''' + fof_year + '''.html" style="color: red">HOME</a></li>
            <li><a href="">FILMS</a></li>
            <li><a href="../../blog.html">BLOGS</a></li>
            <li><a href="../../gallery.html">GALLERY</a></li>
            <li><a href="../../schedule.html">SCHEDULE</a></li>
          </ul>
          <h1 class="logo">
            <img
              src="../../../assets/Image/pfc-logo-wp.png"
              alt=""
              class="logo-img"
            />
          </h1>
        </div>
      </nav>
      <main>
        <div>
          <div class="top-header">
            <p style="font-weight: 700; font-size: 18px">
              NAME OF THE MOVIE: <span class='black' id='film_name'>''' + str(csvfile["MOVIE_NAME"].values[i]) + '''</span>
            </p>
            <br />
            <p style="font-weight: 700; font-size: 15px">
              DIRECTED BY: <span class='black' id='director'>''' + str(csvfile["DIRECTOR"].values[i]) + '''</span>
            </p>
          </div>
          <br />
          <div>
            <div class="wrapper-main">
              <div class="wrapper">
                <i class="fa fa-angle-left" id="left" aria-hidden="true"></i>
                <div class="carousel">
                  <img
                    src="./images/''' + file_name + '''/poster.webp"
                    alt="img"
                    draggable="false"
                  />
                  <img
                    src="./images/''' + file_name + '''/still_1.webp"
                    alt="img"
                    draggable="false"
                  />
                  <img
                    src="./images/''' + file_name + '''/still_2.webp"
                    alt="img"
                    draggable="false"
                  />
                  <img
                    src="./images/''' + file_name + '''/still_3.webp"
                    alt="img"
                    draggable="false"
                  />
                  <img
                    src="./images/''' + file_name + '''/still_4.webp"
                    alt="img"
                    draggable="false"
                  />
                </div>
                <i class="fa fa-angle-right" id="right" aria-hidden="true"></i>
              </div>
            </div>
          </div>
          <br />
          <div class="other-information">
            <p class="heading">SYNOPSIS</p>
            <br />
            <p><span>DURATION</span> <span class='black' id='duration'>''' + str(int(csvfile["MIN"].values[i])) + '''</span> mins</p>
            <p><span>YEAR</span> <span class='black' id='year'>''' + str(int(csvfile["YEAR"].values[i])) + '''</span></p>
            <p><span>COUNTRY</span> <span class='black' id='country'>''' + str(csvfile["COUNTRY"].values[i]) + '''</span></p>
            <p><span>LANGUAGE</span> <span class='black' id='language'>''' + str(csvfile["LANGUAGE"].values[i]) + '''</span></p>
            <br />
            <span class='black' id='plot'>
              <p class="text-justify">
                ''' + str(csvfile["PLOT"].values[i]) + '''
              </p>
            </span>
            <br />
            <p class="heading">ABOUT THE DIRECTOR</p>
            <br />
            <p class="text-justify" id='director_info'>
              ''' + str(csvfile["DIRECTOR_DETAILS"].values[i]) + '''
            </p>
            <br />
            <p class="heading">PERSONNEL</p>
            <br />
  ''' + (("<p><span>Cinematographer</span> <span class='black' id='cinematographer'>" + str(csvfile["CINEMATOGRAPHER"].values[i]) + "</span></p>") if csvfile["CINEMATOGRAPHER"].values[i] != '' else '') + '''
  ''' + (("<p><span>Editor</span> <span class='black' id='editor'>" + str(csvfile["EDITOR"].values[i]) + "</span></p>") if csvfile["EDITOR"].values[i] != '' else '') + '''
  ''' + (("<p><span>Production Designer</span> <span class='black' id='prod_design'>" + str(csvfile["PRODUCTION DESIGN"].values[i]) + "</span></p>") if csvfile["PRODUCTION DESIGN"].values[i] != '' else '') + '''
  ''' + (("<p><span>Sound Designer</span> <span class='black' id='sound_design'>" + str(csvfile["SOUND"].values[i]) + "</span></p>") if  csvfile["SOUND"].values[i] != '' else '') + '''
  ''' + (("<p><span>Sound Mixing and additional design</span> <span class='black' id='sound_mixing'>" + "</span></p>") if False else '') + '''
  ''' + (("<p><span>Background Score</span> <span class='black' id='bg_score'>" + "</span></p>") if False else '') + '''
  ''' + (("<p><span>Colorist</span> <span class='black' id='colorist'>" + str(csvfile["COLORIST"].values[i]) + "</span></p>") if  csvfile["COLORIST"].values[i] != '' else '') + '''
  ''' + (("<p><span>Producer(s)</span> <span class='black' id='producer'>" + str(csvfile["PRODUCER"].values[i]) + "</span></p>") if  csvfile["PRODUCER"].values[i] != '' else '') + '''
           </div>
        </div>
        <br /><br /><br />
      </main>
      <!-- Footer -->
      <footer>
        <div style="line-height: 1.6">
          <form
            method="POST"
            action="https://script.google.com/macros/s/AKfycbyuSNRX24eMn7j0YcwkBkNk9kSE18-mNfSnySbIMXcqqk28N3NrHFli1IEuC8tvJTZEKw/exec"
            name="pfc_contact"
            target="hiddenIframe"
          >
            <p class="get-in-touch-text">GET IN TOUCH</p>
            <label for="" class="label-heading">Name</label> <br />
            <input type="text" class="form-input" /> <br />
            <label for="" class="label-heading">Email</label> <br />
            <input type="email" class="form-input" /> <br />
            <label for="" class="label-heading">Subject</label> <br />
            <input type="text" class="form-input" /> <br />
            <label for="" class="label-heading">Message</label> <br />
            <textarea rows="12" cols="42"></textarea>
            <br />
            <input type="submit" class="submit-button" />
          </form>
        </div>
        <div class="line-horizontal"></div>
        <div class="footer-subtext">
          <div>
            <p class="sub-header">CONTACT US</p>
            <p class="sub-header-text">EMAIL - <a href='mailto:peoplesfilmcollective@gmail.com' style="text-decoration: none; color: white;">peoplesfilmcollective@gmail.com</a></p>
            <p class="sub-header-text">PHONE - <a href='tel:+919163736863' style="text-decoration: none; color: white;">+91 91637 36863</a></p>
          </div>
          <br /><br />
          <div>
            <p class="sub-header">CONTACT WITH US</p>
            <div>icons</div>
            <br /><br />
          </div>
          <div>
            <div class="footer-links">
              <a href="./index.html" style="text-decoration: none; color: white"
                >HOME &nbsp;|&nbsp;
              </a>
              <a
                href="./notice-board.html"
                style="text-decoration: none; color: white"
                >NOTICE BOARD &nbsp;|&nbsp;
              </a>
              <a
                href="./in-the-news.html"
                style="text-decoration: none; color: white"
                >IN THE NEWS
              </a>
            </div>
            <div class="footer-links">
              <a
                href="./publications.html"
                style="text-decoration: none; color: white"
                >PUBLICATIONS &nbsp;|&nbsp;
              </a>
              <a
                href="./support-us.html"
                style="text-decoration: none; color: white"
                >SUPPORT US &nbsp;|&nbsp;
              </a>
              <a
                href="./location.html"
                style="text-decoration: none; color: white"
                >LOCATION</a
              >
            </div>
          </div>
        </div>
      </footer>
      <p class="copyright">© Copyright - People's Film Collective</p>
      <!-- Footer -->
      <iframe
        name="hiddenIframe"
        width="0"
        height="0"
        style="display: none"
      ></iframe>
    </body>
    <script src="../../assets/JS/single-page.js"></script>
    <script type='text/javascript'>
      
    </script>
  </html>'''

  html_file.write(file_contents)
  html_file.close()
