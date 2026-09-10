/* IAQ deck — presenter layer.
   Navigation, present mode, overview, timer, blackout and deep links.
   Slide geometry comes from container-query units, so a cloned slide
   dropped into a small box scales itself: the overview needs no transform. */
(function(){
  var deck     = document.getElementById('deck');
  var stages   = Array.prototype.slice.call(document.querySelectorAll('.stage'));
  var counter  = document.getElementById('counter');
  var bar      = document.getElementById('bar');
  var timerEl  = document.getElementById('timer');
  var overview = document.getElementById('overview');
  var ovGrid   = document.getElementById('ovGrid');
  var help     = document.getElementById('help');
  var blackout = document.getElementById('blackout');
  var total    = stages.length;
  var current  = 0;
  var built    = false;
  var jump     = '';
  var jumpTid  = null;

  function pad(n){ return (n < 10 ? '0' : '') + n; }

  /* ---------------------------------------------------------------- titles */
  var scratch = document.createElement('div');
  function titleOf(stage){
    if (stage.querySelector('.cover-title')) return 'Cover';
    var s = stage.querySelector('.s-title, .div-title, .hero-title');
    if (!s) return 'Slide';
    scratch.innerHTML = s.innerHTML.replace(/<br\s*\/?>/gi, ' ');
    return scratch.textContent.replace(/\s+/g, ' ').trim();
  }
  function numberOf(stage){
    var t = stage.querySelector('.tab');
    return t ? t.textContent.trim() : '';
  }

  /* ---------------------------------------------------------------- moving */
  function paint(){
    counter.textContent = pad(current + 1) + ' / ' + total;
    bar.style.width = ((current + 1) / total * 100) + '%';
    if (built){
      var cards = ovGrid.children;
      for (var i = 0; i < cards.length; i++){
        cards[i].classList.toggle('on', i === current);
      }
    }
    if (history.replaceState) history.replaceState(null, '', '#' + (current + 1));
  }

  function go(i, instant){
    current = Math.max(0, Math.min(total - 1, i));
    stages[current].scrollIntoView({
      behavior: instant ? 'auto' : (motionOK() ? 'smooth' : 'auto'),
      block: 'center'
    });
    paint();
  }
  function motionOK(){
    return !window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /* ---------------------------------------------------------------- overview */
  function build(){
    if (built) return;
    stages.forEach(function(stage, i){
      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'ov-card';
      card.setAttribute('aria-label', 'Go to slide ' + (i + 1) + ': ' + titleOf(stage));

      var frame = document.createElement('span');
      frame.className = 'ov-frame';
      var clone = stage.querySelector('.slide').cloneNode(true);
      clone.removeAttribute('id');
      frame.appendChild(clone);

      var meta = document.createElement('span');
      meta.className = 'ov-meta';
      meta.innerHTML = '<span class="ov-n">' + pad(i + 1) + '</span>' +
                       '<span class="ov-t"></span>';
      meta.querySelector('.ov-t').textContent = titleOf(stage);

      card.appendChild(frame);
      card.appendChild(meta);
      card.addEventListener('click', function(){ closeOverview(); go(i, true); });
      ovGrid.appendChild(card);
    });
    built = true;
  }
  function openOverview(){
    build();
    overview.hidden = false;
    document.body.classList.add('modal-open');
    paint();
    var on = ovGrid.querySelector('.ov-card.on');
    if (on) on.scrollIntoView({block: 'nearest'});
  }
  function closeOverview(){
    overview.hidden = true;
    document.body.classList.remove('modal-open');
  }
  function toggleOverview(){ overview.hidden ? openOverview() : closeOverview(); }

  /* ---------------------------------------------------------------- present */
  function inFull(){ return !!(document.fullscreenElement || document.webkitFullscreenElement); }
  function toggleFull(){
    if (inFull()){
      (document.exitFullscreen || document.webkitExitFullscreen).call(document);
    } else {
      var el = document.documentElement;
      (el.requestFullscreen || el.webkitRequestFullscreen).call(el);
    }
  }
  function syncFull(){
    document.body.classList.toggle('presenting', inFull());
    // the slide box changes size, so re-centre on the current slide
    setTimeout(function(){ go(current, true); }, 60);
  }
  document.addEventListener('fullscreenchange', syncFull);
  document.addEventListener('webkitfullscreenchange', syncFull);

  /* ---------------------------------------------------------------- timer */
  var elapsed = 0, since = null, tick = null;
  function fmt(ms){
    var s = Math.floor(ms / 1000);
    return pad(Math.floor(s / 60)) + ':' + pad(s % 60);
  }
  function shown(){ return elapsed + (since ? Date.now() - since : 0); }
  function draw(){ timerEl.textContent = fmt(shown()); }
  function run(){
    since = Date.now();
    timerEl.classList.add('running');
    if (!tick) tick = setInterval(draw, 500);
    draw();
  }
  function pause(){
    if (since){ elapsed += Date.now() - since; since = null; }
    timerEl.classList.remove('running');
    if (tick){ clearInterval(tick); tick = null; }
    draw();
  }
  function toggleTimer(){ since ? pause() : run(); }
  function resetTimer(){ elapsed = 0; since = null; pause(); run(); }
  timerEl.addEventListener('click', resetTimer);
  timerEl.title = 'Elapsed time — click to reset, T to pause or resume';

  /* ---------------------------------------------------------------- chrome */
  var idle = null;
  function wake(){
    document.body.classList.remove('idle');
    clearTimeout(idle);
    idle = setTimeout(function(){
      if (document.body.classList.contains('presenting') && overview.hidden){
        document.body.classList.add('idle');
      }
    }, 2600);
  }
  document.addEventListener('mousemove', wake);
  document.addEventListener('keydown', wake);

  /* ---------------------------------------------------------------- input */
  document.getElementById('next').addEventListener('click', function(){ go(current + 1); });
  document.getElementById('prev').addEventListener('click', function(){ go(current - 1); });
  document.getElementById('btn-grid').addEventListener('click', toggleOverview);
  document.getElementById('btn-full').addEventListener('click', toggleFull);
  document.getElementById('btn-help').addEventListener('click', function(){
    help.hidden = !help.hidden;
  });
  document.getElementById('ov-close').addEventListener('click', closeOverview);
  blackout.addEventListener('click', function(){ blackout.hidden = true; });

  document.addEventListener('keydown', function(e){
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;

    if (!blackout.hidden && k !== 'b' && k !== 'B'){ blackout.hidden = true; return; }

    if (k >= '0' && k <= '9'){                       // type a number, then Enter
      jump += k;
      counter.textContent = '→ ' + jump;
      clearTimeout(jumpTid);
      jumpTid = setTimeout(function(){ jump = ''; paint(); }, 1400);
      return;
    }
    if (k === 'Enter' && jump){
      e.preventDefault();
      var n = parseInt(jump, 10); jump = '';
      closeOverview();
      go(n - 1);
      return;
    }

    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'ArrowDown'){
      e.preventDefault(); closeOverview(); go(current + 1);
    } else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'ArrowUp'){
      e.preventDefault(); closeOverview(); go(current - 1);
    } else if (k === 'Home'){ e.preventDefault(); go(0); }
    else if (k === 'End'){ e.preventDefault(); go(total - 1); }
    else if (k === 'f' || k === 'F'){ e.preventDefault(); toggleFull(); }
    else if (k === 'o' || k === 'O'){ e.preventDefault(); toggleOverview(); }
    else if (k === 'b' || k === 'B'){ e.preventDefault(); blackout.hidden = !blackout.hidden; }
    else if (k === 't' || k === 'T'){ e.preventDefault(); toggleTimer(); }
    else if (k === '?' || k === 'h' || k === 'H'){ e.preventDefault(); help.hidden = !help.hidden; }
    else if (k === 'Escape'){
      if (!help.hidden){ help.hidden = true; }
      else if (!overview.hidden){ closeOverview(); }
      else if (inFull()){ toggleFull(); }
    }
  });

  /* swipe */
  var x0 = null, y0 = null;
  deck.addEventListener('touchstart', function(e){
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY;
  }, {passive: true});
  deck.addEventListener('touchend', function(e){
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    var dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy)) go(current + (dx < 0 ? 1 : -1));
    x0 = y0 = null;
  }, {passive: true});

  /* ---------------------------------------------------------------- sync */
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting){
          current = stages.indexOf(entry.target);
          paint();
        }
      });
    }, {threshold: 0.6});
    stages.forEach(function(s){ io.observe(s); });
  }

  window.addEventListener('hashchange', function(){
    var n = parseInt((location.hash || '').replace('#', ''), 10);
    if (n > 0 && n <= total && n - 1 !== current) go(n - 1, true);
  });

  /* A deep link has to be re-asserted: the first jump can happen before
     fonts and images settle, and the relayout drops the scroll back. */
  var start = parseInt((location.hash || '').replace('#', ''), 10);
  if (start > 0 && start <= total){
    var target = start - 1;
    var land = function(){ go(target, true); };
    land();
    requestAnimationFrame(land);
    window.addEventListener('load', function(){ land(); setTimeout(land, 250); });
    setTimeout(land, 600);
  } else {
    paint();
  }
  run();
  wake();
})();
