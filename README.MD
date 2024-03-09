# Tubes Stima 1 by Savage
> 'Diamonds' game bot implementation written in Python. Based on the concept of Greedy algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Greedy Strategy](#greedy-strategy)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to our GitHub Repository!

This project was created by:
| No. | Name | Student ID |
| :---: | :---: | :---: |
| 1. | Nelsen Putra | 13520130 |
| 2. | Muhammad Gilang Ramadhan | 13520137 |
| 3. | Naufal Baldemar Ardanni | 13521154 |


## General Information
Diamonds is a programming challenge that pits the bot you create against bots from other players. Each player will have a bot where the goal of this bot is to collect as many diamonds as possible. The way to collect diamonds will not be that simple, of course there will be various obstacles that will make this game more exciting and complex. To win the match, each player must implement a certain strategy on each bot.

There are some components which exist in the game, they are diamonds, red button, teleporterts, bots and bases, and inventory. Our task here is to implement a bot in the game 'Diamonds' by applying the Greedy algorithm strategy to win the game. The strategy must consider all the existing game components mentioned before. To implement with these bots, we are advised to use the available game engine and continue developing the program written in the starter-bots at bot starter-pack.

This Diamonds game bot implementation program was developed in Python language. The game specification that was used to build this bot is based on the Diamonds game rules written in the specification document and [Diamond game starting kit](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit).


## Technologies Used
The whole car bot implementation program was written in Python.


## Greedy Strategy
### Strategi Pemrioritasan Pengumpulan Diamond
Strategi Pemrioritasan Pengumpulan Diamond merupakan strategi untuk memaksimalkan jumlah diamond yang ada di inventory dengan cara mempertimbangkan besar profit yang dihasilkan jika mengambil suatu pergerakan. Melalui strategi ini bot akan memilih untuk bergerak pada grid yang menghasilkan diamond paling banyak dan tidak di-tackle oleh lawan sesaat setelah mengambil diamond tersebut.

### Strategi Pemrioritasan Perlindungan 
Strategi Pemrioritasan Perlindungan merupakan strategi untuk memaksimalkan penghindaran terhadap pergerakan ke grid yang berpotensi untuk di-tackle oleh lawan jika bergerak menuju grid tersebut. Kemudian, dilakukan juga pengambilan grid yang berpotensi menghasilkan profit. Dengan begitu, strategi ini melindungi bot dari adanya ancaman pencurian diamond oleh bot lawan atau player lain.

### Strategi Pemrioritasan Kembali ke Base
 Strategi Pemrioritasan Kembali ke Base merupakan strategi untuk memaksimalkan kemungkinan untuk melakukan gerakan perpindahan menuju base berdasarkan jarak terdekat antara bot dan profit, keamanan bot, serta ketersediaan diamond yang akan disimpan ke base pada setiap state yang akan dilalui oleh bot. Strategi ini mencari prioritas utama bot apakah akan kembali ke base atau tidakn sesuai kondisi inventory dan lingkungan sekitar bot.

### Strategi Pemrioritasan Penyerangan terhadap Lawan
Strategi Pemrioritasan Penyerangan terhadap Lawan merupakan strategi untuk memaksimalkan pengambilan grid yang dapat berpotensi mengambil diamond terbanyak dari bot musuh di sekitar. Dalam hal ini, juga harus diminimalisir kemungkinan bot kita untuk ditabrak oleh Bot lainnya, mengingat pertandingan yang dilakukan melibatkan banyak bot sekaligus.

### Strategi Pemrioritasan Potensi Profit 1 State ke Depan
Strategi Pemrioritasan Potensi Profit 1 State ke Depan merupakan strategi untuk memaksimalkan jumlah potensi profit yang akan dihasilkan pada 1 state selanjutnya melalui peninjauan terhadap state setelah teleport atau terhadap suatu grid yang pada suatu state tetangganya tidak terdapat diamond. Dengan demikian, sebenarnya state tersebut dapat menghasilkan profit pada state tetangga dari state tetangga tersebut.

### Pemilihan Strategi Greedy
Berdasarkan eksplorasi alternatif Algoritma Greedy di atas, kelompok kami memutuskan untuk menggabungkan strategi-strategi tersebut. Hal yang menjadi pertimbangan utama atas keputusan itu adalah fakta bahwa setiap strategi di atas hanya efektif dan dapat digunakan dalam beberapa kasus saja untuk setiap rondenya. Dengan demikian, penggabungan strategi-strategi tersebut dinilai lebih mampu secara efektif untuk menangani seluruh kasus atau skema yang ada selama permainan ketimbang memilih salah satu yang terbaik di antaranya.

Pada implementasi program, akhirnya kami menggabungkan dan memodifikasi kelima strategi tersebut. Untuk menangani kasus-kasus tertentu, kami berpikir bahwa diperlukan adanya pengaturan urutan prioritas strategi yang kemudian coba kami kombinasikan untuk menemukan mana kombinasi urutan yang paling optimal. Hasil yang kelompok dapatkan ialah kombinasi strategi dengan urutan sebagai berikut: 

Urutan prioritas yang kami tentukan terakhir kali berasal dari proses trial and error yang kami ujikan pada reference bot. Hasilnya, prioritas yang disusun demikian menghasilkan win rate tertinggi dibandingkan dengan variasi-variasi lainnya. Berdasarkan pengujian yang telah kami lakukan juga, terdapat kondisi-kondisi tertentu yang tidak dapat dihindari dalam mempengaruhi hasil akhir dari permainan Diamonds ini, misalnya, penempatan posisi bot dan diamond secara random pada awal permainan dan saat terjadi regenerasi diamond melalui red button.


## Setup
### Installation & Requirement
- Download and install [Python](https://www.python.org/downloads/)
- Download and install [NodeJS](https://nodejs.org/en/download/)
- Download and install Yarn
```
npm install --global yarn
```
- Download the whole folders and files in this repository or do clone the repository
- Download Diamonds [Game Engine](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)
- Download Diamonds [Starter Pack](https://github.com/haziqam/tubes1-IF2211-bot-starter-pack/releases/tag/v1.0.1)

### Setup & Execution
The complete setup instructions is written on [Get Started with Diamonds](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit).


## Project Status
Project is: _complete_

All the specifications were implemented.


## Room for Improvement
- A faster or more efficient algorithm to make the program run quicker
- A superior and more advanced strategy to increase the chances of winning the game


## Acknowledgements
- This project was based on [Spesifikasi Tugas Besar 1 IF2211 Strategi Algoritma](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2023-2024/Tubes1-Stima-2024.pdf)
- Thanks to God
- Thanks to Mrs. Nur Ulfa Maulidevi, Mr. Rila Mandala and Mr. Rinaldi as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Big Project for IF2211 Algorithm Strategies


## Contact
Created by Savage. 2024 All Rights Reserved.
