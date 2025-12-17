---
title: "Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer"
date: 2025-12-16T16:53:11+00:00
draft: true
tags: ["U-Net", "Medical Imaging", "ArXiv", "Auto-generated"]
author: "Adarsha Shrestha, Basanta Pokharel, Binit Shrestha et al."
---

## 📝 Abstract

Nepali, a low-resource language spoken by over 32 million people, continues to face challenges in natural language processing (NLP) due to its complex grammar, agglutinative morphology, and limited availability of high-quality corpora. Most efforts to date have centered on basic encoder architectures; they remain insufficient for Nepali-specific text generation. This study presents a GPT-2-based Nepali language model trained using several training strategies inspired by GPT-3, including optimized learning rate schedules, batch scaling, and architectural refinements. A custom 16k Byte-Pair Encoding (BPE) tokenizer was trained exclusively on Nepali text to ensure more consistent segmentation and improved input representation. The model was pretrained on a combined dataset comprising a 10.75GB cleaned NepBERTa corpus and additional web-scraped Nepali news articles. FlashAttention was integrated to reduce memory usage and stabilize training. After two epochs, the model achieved a training loss of 3.168177, a validation loss of 3.081982, and a final perplexity of 21.80, demonstrating its capability to generate coherent Nepali news-style text.

## 📎 Link

[View on ArXiv](https://arxiv.org/abs/2512.14585v1)

## ✍️ Review

*(Write your review here)*
