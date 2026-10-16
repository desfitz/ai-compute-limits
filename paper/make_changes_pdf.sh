#!/bin/bash
# Usage: ./make_changes_pdf.sh old.tex new.tex  -> CHANGES.pdf with additions in blue, deletions in red (needs latexdiff + pdflatex)
latexdiff --type=CFONT --exclude-textcmd="section,subsection,paragraph" --append-safecmd="verify" "$1" "$2" > CHANGES.tex
for i in 1 2 3; do pdflatex -interaction=nonstopmode CHANGES.tex >/dev/null; done
echo "CHANGES.pdf written"
