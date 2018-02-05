function initPage() {

    //initialize list for user data
    var options = {
        valueNames: [ 'name', 'description', 'size' ]
    };
    var userDataList = new List('userData', options);

    //initialize list for community data
    var options = {
        valueNames: [ 'name', 'description', 'size' ]
    };
    var userDataList = new List('communityData', options);

}