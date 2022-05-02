var select = document.querySelector('select');
var button = document.querySelector('button');

select.addEventListener('change', function() {
    document.location.href = '/universities/' + this.value;
});
