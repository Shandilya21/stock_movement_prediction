<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Shandilya21/stock_movement_prediction">
    <img src="plot/Plot_stock.png" alt="Logo" width="350" height="350">
  </a>

  <h3 align="center">Predictive Model for Stock Price Movement</h3>
<!-- 
  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>

 -->

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]] -->
This is a implementation of stock price movement considering the basic and fundamental analysis of stock market. Here, We consider Apple Inc. (APPL:NYSE) quarterly stock price to train our machine learning algorithms. The predicted value is close to the final actual price and hence it will also be reciprocated for more 'stocks', for eg: Microsoft (MSFT: NYSE), Google (GOOG,: NYSE) etc.   

Taking a deep dive interest in stock and market price movement, it is almost difficult for trader to predict to study the market analysis for studyong the important factors. Here we incorporated a end to end LSTM (Long Short Term Memory Network) algorithms to predict the price movement for refernce stock. Also it can compareable with multiple stocks before making an decision.

why we need this?:
* Anyone can effectively save money or 'bad bid' by visualizing stock trend. 
* Brokerage fees would be saved! Anyone with basic utility can make suitable decision


### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [Keras Backened TF](https://keras.io/)
* [Scikit-Learn](https://scikit-learn.org/)


<!-- GETTING STARTED -->
## Getting Started
Below the the basic step to reproduce the code with few commands.

1. Clone the repository
```
git clone https://github.com/Shandilya21/stock_movement_prediction.git

```

### Prerequisites
```
pip install -r requirement.txt
```

<!-- USAGE EXAMPLES -->
## Usage

The code is working for Apple Inc. srock price, Also you can produce results for other sock prices and amake a comparable plot. The default number of epochs = 5. Feel free to set the epochs from Stockprediction.py. 

```
python3 Stockprediction.py   
```
## Results

<br />
<p align="center">
  <a href="https://github.com/Shandilya21/stock_movement_prediction">
    <img src="plot/predicted_stock_price.png" alt="Logo" width="500" height="500">
  </a>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Shandilya21/stock_movement_prediction/issues) for a list of proposed features (and known issues). Also, if you have any issue, feel free to open a new issue.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the project such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git build -b build/newfeature`)
3. Commit your Changes (`git commit -m 'Add some newfeature'`)
4. Push to the Branch (`git push origin build/newfeature`)
5. Open a Pull Request

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE` for more information.
 -->


<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/shandilyaarunav?lang=en) - arunavshandilya96@gmail.com

<!-- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->



<!-- ACKNOWLEDGEMENTS
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)
 -->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/Shandilya21/stock_movement_prediction/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: plot/predicted_stock_price.png
 -->