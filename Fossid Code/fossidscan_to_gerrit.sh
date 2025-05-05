# This script is to display the scan results and the information to the gerrit review.
echo "gerrit project"
echo $GERRIT_PROJECT
echo "fossid scan result"
echo $FOSSID_SCAN_RESULT
echo "gerrit patchset revision"
echo $GERRIT_PATCHSET_REVISION
echo "gerrit environment used"
echo $GERRIT_ENV
# Getting  the match_type value and checking weather the scan is success or failure
match_type=$(echo $FOSSID_SCAN_RESULT | jq '.[].match_type')
id=$(echo $FOSSID_SCAN_RESULT | jq '.[].scan_id')
scan_id="$(echo $id | cut -d' ' -f1 | sed 's/"//g')"
echo "The scan id value is "$scan_id
VALUE="The Fossid scan is successful. The link to view the scan results are https://fossid.comcast.com/webapp/index.php?form=scan&sid=$scan_id For further questions please send an email to open-source-support@rdklistmgr.ccp.xcal.tv"
echo $VALUE
if [ "$match_type" = '"none"' ]
then
    #This executes when the scan provides success scenario
    echo "The scan is successful"
    ssh -p 29418 $GERRIT_ENV gerrit review -p $GERRIT_PROJECT -m "'$VALUE'" $GERRIT_PATCHSET_REVISION --label Fossid-Scan=1
else
    #This executes when the scan provides failure scenario
    echo "The scan has been failed"
    ssh -p 29418 $GERRIT_ENV gerrit review -p $GERRIT_PROJECT -m "'$VALUE'" $GERRIT_PATCHSET_REVISION --label Fossid-Scan=-1
fi
