" Wrap too long lines
set wrap

" Tabs are 4 characters
set tabstop=4

" (Auto)indent uses 4 characters
set shiftwidth=4

" spaces instead of tabs
set expandtab

" guess indentation
"set autoindent

" Expand the command line using tab
set wildchar=<Tab>

" show line numbers
"set number

" Fold using markers {{{
" like this
" }}}
set foldmethod=marker

" enable all features
set nocompatible

" powerful backspaces
set backspace=indent,eol,start

" highlight the searchterms
set hlsearch

" jump to the matches while typing
" set incsearch

" ignore case while searching
set ignorecase

" dont wrap words
set textwidth=78

" history
set history=50

" 1000 undo levels
set undolevels=1000

" show a ruler
set ruler

" show partial commands
set showcmd

" show matching braces
set showmatch

" write before hiding a buffer
set autowrite

"syntax highlight
syntax on

" set colorscheme
" colorscheme borland

" Always show the menu, insert longest match
set completeopt=menuone,longest

" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid or when inside an event handler
" (happens when dropping a file on gvim).
autocmd BufReadPost *
  \ if line("'\"") > 0 && line("'\"") <= line("$") |
\   exe "normal g`\"" |
\ endif

" save a session and restart it later --- always save to ~/.vim_session
":map <F2> :wa<CR>:mksession! ~/.vim_session<CR>
":map <F3> :source ~/.vim_session<CR>

" tab completion with files
set wildmode=longest,list,full
set wildmenu

" ctags
set tags=./tags
set tags+=~/.vim/tags/perls-tags
set tags+=~/.vim/tags/perls-3rd-party-tags

:map <Leader>t :tab split<CR>:exec("tag ".expand("<cword>"))<CR>
:map <Leader>v :vsp <CR>:exec("tag ".expand("<cword>"))<CR>

" toggle spell check on and off
:map <Leader>s :setlocal spell spelllang=en_us<CR>
:map <Leader>S :setlocal nospell<CR>

" to toggle search highlighting
:map <silent> <c-l> :nohls<CR>

" search for selected text, forwards or backwards.
vnoremap <silent> * :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy/<C-R><C-R>=substitute(
  \escape(@", '/\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gV:call setreg('"', old_reg, old_regtype)<CR>
vnoremap <silent> # :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy?<C-R><C-R>=substitute(
  \escape(@", '?\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gV:call setreg('"', old_reg, old_regtype)<CR>

" commands for opening NERDTree in horizontal/vertical split and new tab
:command Se sp %:p:h
:command Ve vs %:p:h
:command Te tabe %:p:h
:command E e %:p:h

" set printer to scribble
set printdevice=scribble

" plugins
filetype plugin on
filetype indent on

source ~/.vim/plugin/hacker_type.vim
source ~/.vim/plugin/matchit.vim
source ~/.vim/plugin/NERD_tree.vim
source ~/.vim/ftplugin/python_match.vim

source $VIMRUNTIME/ftplugin/man.vim
source $VIMRUNTIME/macros/matchit.vim

autocmd BufEnter *.m compiler mlint

