<!-- TITLE: Official Cortex Wiki -->
<!-- SUBTITLE: Your Guide to the AI on Blockchain Ecosystem -->

# Cortex Overview
## What is Cortex?
Cortex is the first ever blockchain technology that allows the execution of AI algorithms on the blockchain. Cortex provides an AI platform for developers to upload their models on the blockchain and be incorporated into smart contracts. The MainNet was launched at the end of June, 2019.

To put it in context, blockchain started with bitcoin, a decentralized digital currency. Then entered Ethereum, which allows programming on top of the blockchain, namely the smart contract. Now Cortex builds on top of Ethereum to enable AI-powered smart contract. 
<img src="/uploads/hiearchy.png" style="width:450px; margin-top: 1%; margin-bottom: 1%; "/>
(The relationship between Cortex, Ethereum, and Bitcoin)

## How does Cortex compare to conventional blockchains like Ethereum?
Right now, conventional blockchains like Ethereum have virtual machines that run on the CPU, which cannot **realistically execute non-trivial AI models.** To incorporate any sort of AI into an Ethereum Dapp, for example, would require running the AI models off-chain, which defeats the purpose of a smart contract. The <a href="https://www.cortexlabs.ai">Cortex team </a> addresses this problem by building a virtual machine that runs on the GPU. This allows AI models to execute directly on the blockchain, enabling **true AI smart contract.** In addition, the CVM is backward-compatible with the EVM, so Ethereum developers can easily migrate their applications onto to the Cortex blockchain and on top of that, incorporate AI models into them.  


## Why do we want to run AI model on the blockchain? Wouldn’t that be very expensive?
Running AI model on the blockchain ensures the integrity of the model. For example, let’s say a smart contract is programmed to give Amy 100 dollars if the facial recognition model recognizes the person as Amy. If the facial recognition model has to run off-chain, its security would be severely compromised: a hacker can change the model to recognize his own face and thereby steal the 100 dollars from the smart contract. On the other hand, if the execution of the facial recognition model happens on the blockchain, it would be very hard to hack the model.  

The transaction fee is extremely low if the network is not super busy. 
What does “Decentralized AI Autonomous Ecosystem” mean? How does Cortex decentralize AI?  

To understand this question, we need to first understand the infrastructure of the Cortex blockchain.

We offer a blockchain platform for AI developers to upload their models and for Dapp developers to easily integrate these models in their Dapps (without the hassle of dealing with different protocols of different AI model service providers). A helpful analogy is to think of Cortex as a decentralized eBay for machine learning model API calls, where the sellers are the AI model providers and the buyers are the Dapp developers. Via smart contracts, AI model provider gets a portion of the transaction fee whenever the model is inferred. 

This creates an ecosystem where individual AI developers, not just big corporations, are incentivized to upload their AI models to the blockchain, and Dapp developers have access to the best AI models in the world and have the freedom to choose between them. Hence the decentralization. The competition within the ecosystem between AI model providers will naturally lead to the evolution of better and better AI models. Hence the term “autonomous ecosystem.”

## Sometimes you use the word “AI” and sometimes you use the word “machine learning”, what is the relationship between these two terms?

Machine learning is a subfield of AI and by far the most promising one in helping achieve better artificial intelligence. The basic idea of machine learning is to train machines to certain perform tasks without explicitly programming them. In our marketing semantics and the machine learning communities in general, they have been used rather interchangeably. 


## Could you please tell me what are the difficulties to run AI models on the blockchain? Why is the deterministic engine so important?
The amount of computation of the AI model exceeds the capabilities of Ethereum's "world computer", so accelerators such as GPUs need to be introduced to speed up the process. 

In today's model inference, there are floating-point numbers and parallel computation parts, which bring uncertainty to the computation results, which is unacceptable when verifying blockchain transactions. The popular quantization method is also not specifically designed to be deterministic. It is therefore necessary to develop an inference engine and a training engine specifically designed for blockchain consensus.

This goal is indeed quite challenging. The main technical difficulties also correspond to the frontier research direction in the Bay Area, including the quantized acceleration method of the deep neural network (DNN) model and the virtualization method adapted to the AI ​​accelerator. The AI industry’s main concern in quantized acceleration research focuses more on speeding up centralized inference and model compression; however, on the blockchain, we need to ensure the deterministic nature of computations. Here, we do not simply use existing frameworks such as Tensorflow, MXNet, or PyTorch, but rather aim to design frameworks optimized for the needs of on-chain inference.

Making engines deterministic has its technical difficulties, considering the cumulative overflow and compatibility with different hardware platforms; we are solving a lot of engineering problems. Only deterministic engines can bring about algorithmic consensus and realize the transparency and immutability of blockchain’s self-verifying mechanism. For example, let’s say an autonomous vehicle got into an accident, the inference for the move that caused the accident must be based on open blockchain consensus to reduce disputes and settle liabilities.


## What Algorithm is used for Proof of Work?
Cuckoo Cycle. 

## How is Cortex different from other AI On Blockchain projects?
We are the only project that allows you to run AI programs on the blockchain realistically. 

## Use Cases for AI on Blockchain?

Games and game AIs (such as Fomo3D or sports betting) are the most likely to be the first mass-market, because they form the shortest closed loop. Fintech blockchain technologies, such as anti-fraud in decentralized exchanges, credit systems, lending and smart investment, will probably be the next biggest market, considering all their data will be stored on the blockchain. In addition, we can realize stablecoin model controlled by AI-model on Cortex, and the on-chain  inference process makes it much more transparent than other stablecoins such as USDT. Furthermore,  decentralized autonomous token distribution, decentralized anonymous advertisement recommendation engine, autonomous driving, native Cortex AI Dapps, and really any mass markets that involve AI will see use cases on Cortex. 


# Cortex Use Cases
* **DeFi: **credit report, anti-fraud in decentralized exchanges, p2p financing, insurance, cryptocurrency lending
* **Gaming:** AI judge, player agent, NPC, assistant/coaching/education
* **Global Climate Action & Carbon Credit Management and Trading:** collects environmental data and puts on the blockchain for a transparent carbon pricing system
* **AI Governance:** stablecoins based on machine learning, sentiment analysis, decentralized decision making, malicious behavior detection, smart resource allocation
* **Others:** on-chain data mining, facial recognition, recommendation, chatbot, machine translation, voice synthesis, etc.

## Specific Use Case Examples
### Defi
For example, a decentralized lending app can run an AI algorithm to determine your interest rate based on your personal credit history. The AI used to analyze your credit score is not a black box, but instead, every step of the AI inference is transparent to prevent discrimination and ensure fairness. 

### Gaming
CryptoKitties would be much cuter, more life-like, and unique if they incorporated AI. Imagine these kitties moving dynamically and behaving uniquely depending on your personal experience interacting with them. While Ethereum is not able to execute AI models and allow for this user experience, this is something that Cortex can uniquely enable.

### Insurance
Blockchain finds many use cases in the insurance industry, where immutability, fairness, openness, and transparency are in high demand. AI can help improve underwriting decisions, better manage risks, and prevent fraud. An insurance DAO powered by on-chain AI can bring us better, cheaper, fairer, and less bureaucratic insurance. 

### Decentralized Uber
Almost every aspect of Uber involves AI, from matching drivers and riders, route optimization, driver onboarding to determining fares. Therefore, if we want to build a decentralized Uber, it is necessary to be able to run AI on the blockchain. 

### Anti-fake AI
The emergence of deepfakes (AI-manipulated videos that are indistinguishable to the human eye) poses a significant threat to society. Social stability will inevitably suffer if video recordings can simply be dismissed as untrustworthy in court. Anti-fake AI algorithms (algorithms that detect whether a video has been tampered with) will run on the blockchain to ensure their transparency and fairness, especially if there were to be used in court. 

The bullet points and specific examples above are only use cases thought of by the Cortex team alone. It is almost certain that the community will conceive many more and better use cases for AI on the blockchain. After all, rarely anyone thought of the best use cases for the internet today when it was first invented.


# Developing on Cortex
## Where can I get started developing on Cortex?
## What is the process to upload AI models to Cortex?


# Mining

## No support for AMD, only for NVDIA?


## Hardware needed to run a Cortex full node?
A 1060 GPU or even a MX150 GPU laptop is enough. We currently have some nodes running the full node. You can check it out at http://monitor.cortexlabs.ai/table-list


## Does your platform support WASM or is WASM compatible?
WASM compatibility is not the focus of the Cortex MainNet, and WASM programming is not directly supported yet. However, if it turns out to be adopted by the blockchain industry mainstream, we will work to support it. We pay very close attention to Ethereum's progress in this regard.




# Community
## How do you attract developers or companies to develop on Cortex? What moves has Cortex made to encourage developers to come?

We treat attracting developers and companies to Cortex as a system project that integrates improving development environment, maintaining user & developer community, and developing Cortex wallet on various platforms. Above all Cortex prioritizes enhancing the development environment, seeking to create a suite of tools analogous to the development ecological layout of XCode/Android Studio for IOS/Android. 

 As of right now there exists rarely any public chain with similar level of developer-friendliness as Ethereum, and we strive to change this by focusing on two general directions.

First, we guarantee a high degree of compatibility with Ethereum. We allow Ethereum developers to migrate their existing Ethereum Dapp to Cortex at almost zero cost and enhance their Dapps by incorporating AI features. This will drastically lower the cost of learning - developers familiar with Ethereum can start developing on Cortex with very little additional learning.

Second, we will highlight Cortex’s new unique computing environment that activates the AI features for Dapps, something remains to be seen by developers and companies. For the first time, developers will be able to create true AI Dapps such as The Master of Digital Clash by inferring models on the chain. 

In addition to the points already mentioned, from the perspective of development, Cortex is an open-source project that will be constantly evolving in accordance to the preferences of developers that build on them. We provide an web IDE for AI Dapp developers, and for model developers, we offer support for computational power, model libraries, and standardized data sets. Our team will continue to work closely with developers to help implement their technologies in various scenarios. 

From the perspective of operation, we will follow up with Hackathons and challenge bounties, activities closely linked to token incentives. In addition, we realize that developers like to interact with leading industry figures through activities such as AMAs and have included these in our operation plans. 


## What tools will you provide to help developers to develop?
We provide an web IDE for AI Dapp developers, and for model developers, we offer support for computational power, model libraries, and standardized data sets. Our team will continue to work closely with developers to help implement their technologies in various scenarios. 









