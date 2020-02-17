"""
how  merge sort works?

        [14, 7, 3, 12,  9, 11, 6, 2]
                ↙️         ↘️               recursively divide in to half
    [14, 7, 3, 12]         [9, 11, 6, 2]
        ↙️   ↘️                ↙️   ↘️      recursively divide in to half
    [14, 7] [3, 12]        [9, 11] [6, 2]
      ↙️↘️   ↙️↘️            ↙️↘️   ↙️↘️    recursively divide in to half
    14  7    3  12          9  11  6  2     this is the base case. when divided in to half, only one element is left
     ↘️        ↙️            ↘️     ↙️      merge
    [7, 14]  [3, 12]      [9, 11] [2, 6]
      ↘️        ↙️         ↘️        ↙️     merge
      [3, 7, 12, 14]       [2, 6, 9, 11]
                ↘️          ↙️              merge
         [2, 3, 6, 7, 9, 11, 12, 14]
"""