# Understanding VADER using LIME
High-complexity Machine Learning models are capable of making really accurate predictions. Sadly, this gain in accuracy is often accompanied by a loss in interpretability. That is, we know _what_ the model predicts, but we do not undesrtand _which_ factors influence the model's decision-making process.

This project uses Local Interpretable Model-agnostic Explanations (LIME) to make sense of VADER - a pretrained Natural Language Processing (NLP) model that measures the degree of negativity in a text.

The LIME approach relies on making local modifications to a given data point to understand how the fitted model responds to these changes.

## Overview
VADER receives a text and, among other things, replies with a score that measures its negativity.

For example, the text
> Dear Dice,
> 
> This game sucks. The specialists are trash. This trailer was a lie. I want my money back.

receives a negative score of `0.112`.

What drove this black-box model to make this prediction? Is it the words _sucks_ and _trash_? Does the word _dear_ reduce the predicted negativity?

The goal of this project is to address these questions by understanding what drives VADER's negative-sentiment score.

I do this in three steps:
1. Mining the comments
2. Using VADER to predict the negative score of each comment
3. Making slight modifications to the comments to backward-engineer the driving factors of the model

## Context
I mined a few thousand comments from Battlefield 2042's [launch trailer](https://www.youtube.com/watch?v=ASzOzrB-a9E).

I picked this video because Battlefield 2042 was a highly-anticipated yet poorly-received game. As stated in [Kotaku](https://kotaku.com/on-steam-farming-simulator-22-has-more-active-players-1848128969):
> One of the biggest games of the year on one of the most popular digital stores in the world on one of the biggest gaming platforms in the world [...] isn't able to keep up with Farming Simulator 22.

As of May 2022, the video has 23 million views and around 100K comments. Due to the game's populatiry and poor reception by the general public, the comment section is large and overwhelmingly negative, making it a good case study for this project.