deck.tex builds the chart-driven deck from the same figures/ as the paper. Rebuild after any figure or number change:
  cd paper && pdflatex deck.tex && pdflatex deck.tex
Numbers quoted on slides are the register's headline numbers (numbers.json); update them with the paper's tables at each version.
