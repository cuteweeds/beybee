SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

if ! command -v gh >/dev/null 2>&1; then
    echo "Install gh first"
    exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
    echo "You are not logged in."
fi

gh cuteweeds
git status

exec $SHELL