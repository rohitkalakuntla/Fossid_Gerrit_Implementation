echo "Start of Fossid Pre work setup"
# Creating a FOSSID folder as everything will be present at single place.
mkdir FOSSID
cd FOSSID
# Cloning the repo where the Fossid code is present.
git clone https://gerrit.teamccp.com/utils/scmtools
# Copying only Fossid related changes
cp -R scmtools/fossid/. .
# Removing the repo which was cloned.
rm -rf scmtools fossidprework_setup.sh
# This is to store all the gerrit patchset
mkdir fossid_scans
chmod 755 get_review_from_gerrit.py fossidscan_to_gerrit.sh fossid.properties fossid_scans
echo "End of script"
