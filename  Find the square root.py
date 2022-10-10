{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Find square root of real or complex numbers\
# Importing the complex math module\
import cmath\
\
num = 1+2j\
\
# To take input from the user\
#num = eval(input('Enter a number: '))\
\
num_sqrt = cmath.sqrt(num)\
print('The square root of \{0\} is \{1:0.3f\}+\{2:0.3f\}j'.format(num ,num_sqrt.real,num_sqrt.imag))\
}