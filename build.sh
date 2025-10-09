#! /bin/sh

set -e

SITE=site

## version

VERS='25.0.0'
TIME=`date -u +%Y%m%d%H%M`
VERS_FULL="${VERS}.${TIME}"

rm -f VERSION-*
echo "v${VERS}" > VERSION-${VERS_FULL}

sed -i "s/--em-vers:.*;/--em-vers: \"${VERS}\";/" docs/extra.css
sed -i "s/--em-time:.*;/--em-time: \"${TIME}\";/" docs/extra.css

rm -rf $SITE
source pyenv/Scripts/activate
mkdocs build -d $SITE
deactivate

