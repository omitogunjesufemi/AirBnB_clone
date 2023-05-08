#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
    cat <<- 'EOF'
    # This file lists all individuals having contributed content to the
      repositiory.
    EOF
    echo
    git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
