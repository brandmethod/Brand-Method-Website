(function(){
  var deck = document.getElementById('deck');
  var stages = Array.prototype.slice.call(document.querySelectorAll('.stage'));
  var counter = document.getElementById('counter');
  var current = 0;

  function pad(n){ return (n < 10 ? '0' : '') + n; }

  function go(i){
    current = Math.max(0, Math.min(stages.length - 1, i));
    stages[current].scrollIntoView({behavior: 'smooth', block: 'center'});
    counter.textContent = pad(current + 1) + ' / ' + stages.length;
  }

  document.getElementById('next').addEventListener('click', function(){ go(current + 1); });
  document.getElementById('prev').addEventListener('click', function(){ go(current - 1); });

  document.addEventListener('keydown', function(e){
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); go(current + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(current - 1); }
    else if (e.key === 'Home') { e.preventDefault(); go(0); }
    else if (e.key === 'End') { e.preventDefault(); go(stages.length - 1); }
  });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting) {
          current = stages.indexOf(entry.target);
          counter.textContent = pad(current + 1) + ' / ' + stages.length;
        }
      });
    }, {threshold: 0.6});
    stages.forEach(function(s){ io.observe(s); });
  }
})();
