\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lipletter}[1998/01/30 LIP Letter style]

\newif\if@hasmargins
\@hasmarginsfalse

\DeclareOption{nomarginnotes}{\@hasmarginsfalse}
\DeclareOption{marginnotes}{\@hasmarginstrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{letter}}
\ProcessOptions\relax

%\LoadClass[a4paper]{letter}
\LoadClass{letter}

% OK. Now let's set the lengths...

% Horizontally. Because the width of the logos will determinate their
% heights
\setlength{\textwidth}{\paperwidth}
\setlength{\oddsidemargin}{0pt}
\setlength{\evensidemargin}{\oddsidemargin}
\setlength{\hoffset}{-1in}
\addtolength{\hoffset}{25mm}
\setlength{\marginparsep}{0pt}
\setlength{\marginparwidth}{0pt}
\if@hasmargins
  \setlength{\marginparsep}{4mm}
  \setlength{\marginparwidth}{23mm}
\else\fi
% 2(\hoffset+1in) (to center the text)
\addtolength{\textwidth}{-50mm}
\addtolength{\textwidth}{-\marginparsep}
\addtolength{\textwidth}{-\marginparwidth}
\addtolength{\textwidth}{-\oddsidemargin}

% Vertically

\setlength{\voffset}{-1in}
\addtolength{\voffset}{15mm}
\setlength{\textheight}{\paperheight}

\setlength{\topmargin}{0pt}
\setlength{\headsep}{8mm}
\setlength{\headheight}{0.15\textwidth}
\setlength{\footskip}{0.15\textwidth}

% 2(\voffset+1in) (to center the text)
\addtolength{\textheight}{-50mm}
\addtolength{\textheight}{-\topmargin}
\addtolength{\textheight}{-\headheight}
\addtolength{\textheight}{-\headsep}
\addtolength{\textheight}{-\footskip}

\RequirePackage{liplogos}




\renewcommand{\ps@firstpage}{%
  \renewcommand{\@oddhead}{%
    \LIPLetterTitle}%
  \renewcommand{\@oddfoot}{%
    \ENSLTitle}}

