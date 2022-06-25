mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = truth\n\
\n\
" > ~/.streamlit/config.toml