/* Fecha obligatoria de hoy */
let dtElem2 = document.getElementById('date');
let minDate2 = new Date();
let maxDate2 = new Date();
minDate2.setDate(maxDate2.getDate() );
maxDate2.setDate(minDate2.getDate() );


dtElem2.min = formatDate(minDate2);
dtElem2.max = formatDate(maxDate2);

console.log(formatDate(minDate2));
console.log(formatDate(maxDate2));


function formatDate(date) {
  let dd = String(date.getDate()).padStart(2, '0');
  let mm = String(date.getMonth() + 1).padStart(2, '0');
  let yyyy = date.getFullYear();
  return yyyy+'-'+mm+'-'+dd;
}



