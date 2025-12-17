---
title: "Segmental Attention Decoding With Long Form Acoustic Encodings"
date: 2025-12-16T18:12:37+00:00
draft: true
tags: ["U-Net", "Medical Imaging", "ArXiv", "Auto-generated"]
author: "Pawel Swietojanski, Xinwei Li, Mingbin Xu et al."
---

## 📝 Abstract

We address the fundamental incompatibility of attention-based encoder-decoder (AED) models with long-form acoustic encodings. AED models trained on segmented utterances learn to encode absolute frame positions by exploiting limited acoustic context beyond segment boundaries, but fail to generalize when decoding long-form segments where these cues vanish. The model loses ability to order acoustic encodings due to permutation invariance of keys and values in cross-attention. We propose four modifications: (1) injecting explicit absolute positional encodings into cross-attention for each decoded segment, (2) long-form training with extended acoustic context to eliminate implicit absolute position encoding, (3) segment concatenation to cover diverse segmentations needed during training, and (4) semantic segmentation to align AED-decoded segments with training segments. We show these modifications close the accuracy gap between continuous and segmented acoustic encodings, enabling auto-regressive use of the attention decoder.

## 📎 Link

[View on ArXiv](https://arxiv.org/abs/2512.14652v1)

## ✍️ Review

*(Write your review here)*
