/* Fecha maxima 30 dias despues */
let dtElem = document.getElementById('fechaterm');
let minDate = new Date();
let maxDate = new Date();
minDate.setDate(maxDate.getDate() + 30);
maxDate.setDate(minDate.getDate() + 31);


dtElem.min = formatDate(minDate);
dtElem.max = formatDate(maxDate);

console.log(formatDate(minDate));
console.log(formatDate(maxDate));


function formatDate(date) {
  let dd = String(date.getDate()).padStart(2, '0');
  let mm = String(date.getMonth() + 1).padStart(2, '0');
  let yyyy = date.getFullYear();
  return yyyy+'-'+mm+'-'+dd;
}


