function DtTimeDiff(sender, args) {
    var startDate = Date.parse(document.getElementById('datefield').value);
    var endDate = Date.parse(document.getElementById('datefield').value);
    var timeDiff = endDate - startDate;

    daysDiff = Math.floor(timeDiff / (1000 * 60 * 60 * 24));

    if (daysDiff > 90) {
        args.IsValid = false;
    }
    else {
        args.IsValid = true;
    }

}