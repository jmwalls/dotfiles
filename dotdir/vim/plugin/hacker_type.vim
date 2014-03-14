" hacker type vim script
" inserts random src code when enabled
" 
" Jeff Walls <jmwalls@umich.edu>
" January 20, 2012

" ensure we only run once
if exists ('loaded_hackerType')
    finish
endif
let loaded_hackerType = 1

" map keys to hacker type
if !hasmapto('<Plug>HackerType')
    map <silent> <unique> <Leader>h <Plug>HackerType
endif
noremap <unique> <script> <Plug>HackerType <SID>HackerType
noremap <SID>HackerType :call <SID>HackerType()<CR>

" hacker type
function s:HackerType()
python <<EOF
import vim

def get_input ():
    vim.command ('let ch = getchar ()')
    return vim.eval ('ch')

def hacker_type (line, row):
    # print current line
    old = vim.current.buffer[row-1]
    vim.current.buffer[row-1:row] =  [old + line]

def parse_line (line):
    if len (line) > 4:
        ind = 3
    else:
        ind = len (line)
    return line[:ind], line[ind:]

fname = '/home/jeff/perls/src/core/perls-common/generic_sensor_driver.c'
f = open (fname, 'r')

for line in f:
    row, col = vim.current.window.cursor
    while line:
        code, line = parse_line (line)
        ch = get_input ()
        if int (ch) == 27:
            break
        hacker_type (code, row)
        vim.command ('redraw')
    if line:
        break
    vim.current.buffer.append ('')
    row += 1
    vim.current.window.cursor = row, col
f.close ()

EOF

endfunction

