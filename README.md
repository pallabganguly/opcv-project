%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Journal Article
% LaTeX Template
% Version 1.4 (15/5/16)
%
% This template has been downloaded from:
% http://www.LaTeXTemplates.com
%
% Original author:
% Frits Wenneker (http://www.howtotex.com) with extensive modifications by
% Vel (vel@LaTeXTemplates.com)
%
% License:
% CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\documentclass[twocolumn]{article}

\usepackage{blindtext} % Package to generate dummy text throughout this template 

\usepackage[sc]{mathpazo} % Use the Palatino font
\usepackage[T1]{fontenc} % Use 8-bit encoding that has 256 glyphs
\linespread{1.05} % Line spacing - Palatino needs more space between lines
\usepackage{microtype} % Slightly tweak font spacing for aesthetics

\usepackage[english]{babel} % Language hyphenation and typographical rules

\usepackage[hmarginratio=1:1,top=32mm,columnsep=20pt]{geometry} % Document margins
\usepackage[hang, small,labelfont=bf,up,textfont=it,up]{caption} % Custom captions under/above floats in tables or figures
\usepackage{booktabs} % Horizontal rules in tables

\usepackage{lettrine} % The lettrine is the first enlarged letter at the beginning of the text

\usepackage{enumitem} % Customized lists
\setlist[itemize]{noitemsep} % Make itemize lists more compact

\usepackage{abstract} % Allows abstract customization
\renewcommand{\abstractnamefont}{\normalfont\bfseries} % Set the "Abstract" text to bold
\renewcommand{\abstracttextfont}{\normalfont\small\itshape} % Set the abstract itself to small italic text

\usepackage{titlesec} % Allows customization of titles
\renewcommand\thesection{\Roman{section}} % Roman numerals for the sections
\renewcommand\thesubsection{\roman{subsection}} % roman numerals for subsections
\titleformat{\section}[block]{\large\scshape\centering}{\thesection.}{1em}{} % Change the look of the section titles
\titleformat{\subsection}[block]{\large}{\thesubsection.}{1em}{} % Change the look of the section titles

\usepackage{fancyhdr} % Headers and footers
\pagestyle{fancy} % All pages have headers and footers
\fancyhead{} % Blank out the default header
\fancyfoot{} % Blank out the default footer
\fancyhead[C]{CS-892 $\bullet$ Kalyani Government Engineering College $\bullet$ Feb 2018 } % Custom header text
\fancyfoot[RO,LE]{\thepage} % Custom footer text

\usepackage{titling} % Customizing the title section

\usepackage{hyperref} % For hyperlinks in the PDF
\usepackage{graphicx} % For graphs
\graphicspath{ {images/}}

%----------------------------------------------------------------------------------------
%	TITLE SECTION
%----------------------------------------------------------------------------------------

\setlength{\droptitle}{-4\baselineskip} % Move the title up

\pretitle{\begin{center}\huge\bfseries} % Article title formatting
\posttitle{\end{center}} % Article title closing formatting
\title{Performance of Cascade Classifiers used for open hand detection} % Article title
\author{%
\textsc{Aditya Jain} \\ % Your name
\textsc{Pallab K. Ganguly} \\ % Your name
\textsc{Sauradip Nag} \\ % Your name
\textsc{Swati G. Hazra} \\[1ex] % Your name
\normalsize Kalyani Government Engineering College \\ % Your institution
%\normalsize \href{mailto:john@smith.com}{john@smith.com} % Your email address
%\and % Uncomment if 2 authors are required, duplicate these 4 lines if more
%\textsc{Jane Smith}\thanks{Corresponding author} \\[1ex] % Second author's name
%\normalsize University of Utah \\ % Second author's institution
%\normalsize \href{mailto:jane@smith.com}{jane@smith.com} % Second author's email address
}
\date{February 1, 2018} % Leave empty to omit a date
\renewcommand{\maketitlehookd}{%
\begin{abstract}
\noindent {Following our last report, where we pointed out that smaller window sizes were more promising in terms of accuracy, we proceeded to test classifiers of smaller window sizes, with varying number of stages to obtain a working classifier model. This report deals with the description of the evaluation perfomed, its results and interpretation.}
\end{abstract}
}

%----------------------------------------------------------------------------------------

\begin{document}

% Print the title
\maketitle

%----------------------------------------------------------------------------------------
%	ARTICLE CONTENTS
%----------------------------------------------------------------------------------------

\section{Brief description of training of classifiers}

%\lettrine[nindent=0em,lines=3]{L} orem ipsum dolor sit amet, consectetur adipiscing elit.
{From our last series of tests, it was found that with the increase in window size, the number of positive samples successfully detected from a set of 200 images decreased. We therefore proceeded with smaller window size. In particular, we trained two classifiers corresponding to three window sizes:
\begin{itemize}
\item C1: Trained on 20x20 positive images
\item C2: Trained on 30x30 positive images
\item C3: Trained on 40x40 positive images
\end{itemize}
In addition to this a 50x50 classifier was used for benchmarking performance.
Each of the above HAAR type cascade classifier was trained for 15 stages, using GAB algorithm.
}

%------------------------------------------------

\section{Test dataset and performance metric}

The test dataset was created as below:
\begin{enumerate}
\item Raw positive images of hands (both L and R) grayscale, resized to 20x20
\item Superimposed\footnote{Using opencv\_createsamples} on random 100x100 grayscale images, created 500 superimposed images.
\end{enumerate}
We also point out to the reader that the in dataset described above, each image consists exactly one positive image. Thus there are 500 positive images in our dataset. The location of the positives, and the height and width are available in the filename, as serve as a label for the dataset.\\
Once again, we used accuracy as the performance metric, as the dataset was not unfairly skewed. We  define accuracy as the fraction of positive samples correcty detected from the actual number of positives in the dataset. From our previous experience, the optimum threshold a detected region has to cover against the actual region in the image is in the range 70-80 percent. Therefore, we did not vary the threshold in our present test.

%\blindtext % Dummy text

%------------------------------------------------

\section{Parameters varied}

\begin{table}
\caption{Parameters}
\centering
\begin{tabular}{ccc}
\toprule
No. & Parameter & Range \\
\midrule
1 & Scale Factor & $[1.01, 1.02, ..., 2.02]$ \\
2 & Min. Neighbors & $[1, 2, ..., 50]$ \\
3 & No. of  Stages & $[10, 12, 15, 17, 20]$\\
\bottomrule
\end{tabular}
\end{table}

The parameters varied and their ranges are described in Table 1.
%\blindtext % Dummy text

%------------------------------------------------

\section{Algorithm}

\begin{table}
\caption{Algorithm}
\centering
\begin{tabular}{rl}
\toprule
1. & size $\leftarrow$ 500\\
2. & params $\leftarrow$ scale, neighbours, stages\\
3. & vals $\leftarrow$ range of values of params\\
4. & load cascade file\\
5. & for each val in vals do:\\
6. & count $\leftarrow$ 0\\
7. & for each img in training-set do:\\
8. & detectMultiScale(img, params)\\
9. & get predicted region for img, \\
&compare with actual labels\\
10. & if predicted region covers $\geq$ 70\%\\
&actual region, count it as hit.\\
11. & accuracy=hits/size\\
12. & plot accuracy vs. params.\\

\bottomrule
\end{tabular}
\end{table}
The algorithm is described in Table 2. It is virtually the same algorithm as used earlier.
%\blindtext % Dummy text
% \begin{equation}
% \label{eq:emc}
% e = mc^2
% \end{equation}


%------------------------------------------------

\section{Results}

{Figure 1. depicts the variation of accuracy with neighbours, Figure 2. depicts the variation of accuracy with scale. Figure 3 represents the number of positives detected for different stages of classifiers.}
\begin{figure}
\includegraphics[scale=0.5]{fig1}
\caption{Accuracy vs. minNeighbours, scale=1.03, 15 stage classifiers}

\includegraphics[scale=0.5]{fig2}
\caption{Accuracy vs. scaleFactor, minNeighbours=2, 15 stage classifiers}

\includegraphics[scale=0.5]{fig3}
\caption{Positives detected vs. windowSize, scale=1.08, minNeighbours=9, 15 stage classifiers}
\end{figure}

%-------------------------------------------------
\section{Conclusion}
\begin{enumerate}
\item Based on the above evidence, the 20x20 classifier, for 15 stages seems to be the most promising candidate for future work.
\item We also may say that the values of scale factor and min neighbours should be in the range 1.01-1.05 and 2-10 respectively to achieve high accuracy.
\end{enumerate}

%----------------------------------------------------------------------------------------
%	REFERENCE LIST
%----------------------------------------------------------------------------------------

%\begin{thebibliography}{99} % Bibliography - this is intentionally simple in this template

%\bibitem[Figueredo and Wolf, 2009]{Figueredo:2009dg}
%Figueredo, A.~J. and Wolf, P. S.~A. (2009).
%\newblock Assortative pairing and life history strategy - a cross-cultural
%  study.
%\newblock {\em Human Nature}, 20:317--330.
 
%\end{thebibliography}

%----------------------------------------------------------------------------------------

\end{document}
