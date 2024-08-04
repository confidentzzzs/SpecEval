# SpecEval: A Multi-Aspect Benchmark for Specification Generation Across Maturity Levels

## Overview

SpecEval is a benchmarking tool designed to evaluate the capability of large language models (LLMs) in generating formal specifications, including preconditions and postconditions. This project provides resources and tools to assess and enhance the quality of generated specifications.

## Paper

**Title:** SpecEval: A Multi-Aspect Benchmark for Specification Generation Across Maturity Levels  
**Status:** Under Submission

### Abstract

Recent research has shown that large language models (LLMs) are capable of generating formal specifications, including preconditions and postconditions. We propose **SpecEval**, a multi-aspect benchmark to assess the maturity level of existing LLMs for specification generation. It is derived from a diverse set of real-world, open-source projects in Java and Python, including 748 programs sourced from HumanEval, LeetCode, and popular GitHub repositories. We define the maturity level based on the complexity of dependencies of the target code snippet and the complexity of properties being checked, and use specification equivalence checks and testing to calculate the accuracy of generated specifications. Extensive experiments on different prompting strategies and six state-of-the-art models—GPT-4, GPT-3.5, LLaMA-2, LLaMA-3, and CodeLlama—highlight the challenges in generating postconditions for complex logic and external dependencies. Our research finds that generating preconditions and postconditions with high dependency is more challenging than that with self-contained programs, and the language matters for LLMs to generate formal specifications, underscoring the need for further improvements. Our analysis provides insights into the current progress and future directions for enhancing models’ abilities to generate accurate and comprehensive specifications.
