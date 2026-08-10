/* ==========================================================================
   IAQ · BRAND IDENTITY BOOK — deck engine
   --------------------------------------------------------------------------
   Responsibilities
   1. Fit the fixed 1920x1080 stage to any viewport
   2. Page turning (keys, wheel, click, swipe, dock, rail, index)
   3. Direction-aware page-turn animation + red scan sweep
   4. Section rail + progress + auto-built index overlay
   5. Deep-link via #hash, print-safe
   ========================================================================== */
(function () {
  'use strict';

  var stage    = document.getElementById('stage');
  var slides   = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var scan     = document.getElementById('scan');
  var progress = document.querySelector('#progress span');
  var counter  = document.getElementById('count');
  var railBox  = document.getElementById('rail');
  var indexBox = document.getElementById('index');
  var indexWrap= document.querySelector('#index .wrap');
  var dock     = document.getElementById('dock');
  var hint     = document.getElementById('hint');

  var cur = 0, busy = false, total = slides.length;

  /* ---------------------------------------------------------------- fit */
  function fit() {
    var pad = window.innerWidth > 900 ? 0.955 : 1;
    var k = Math.min(window.innerWidth / 1920, window.innerHeight / 1080) * pad;
    stage.style.transform = 'scale(' + k + ')';
  }
  window.addEventListener('resize', fit);

  /* -------------------------------------------------------------- pager */
  function go(n, dir) {
    n = Math.max(0, Math.min(total - 1, n));
    if (n === cur || busy) return;
    dir = dir || (n > cur ? 1 : -1);
    busy = true;

    var from = slides[cur], to = slides[n];

    from.classList.remove('is-active', 'in-next', 'in-prev');
    from.classList.add('is-out', dir > 0 ? 'out-next' : 'out-prev');

    to.classList.remove('is-out', 'out-next', 'out-prev');
    // restart entrance choreography
    to.classList.remove('is-active');
    void to.offsetWidth;
    to.classList.add('is-active', dir > 0 ? 'in-next' : 'in-prev');

    // red scan sweep
    scan.classList.remove('go', 'rev');
    void scan.offsetWidth;
    scan.classList.add('go');
    if (dir < 0) scan.classList.add('rev');

    cur = n;
    sync();

    setTimeout(function () {
      from.classList.remove('is-out', 'out-next', 'out-prev');
      busy = false;
    }, 740);
  }
  function next() { go(cur + 1, 1); }
  function prev() { go(cur - 1, -1); }

  /* ---------------------------------------------------------------- sync */
  function sync() {
    var s = slides[cur];
    progress.style.width = ((cur) / (total - 1) * 100) + '%';
    counter.innerHTML = '<b>' + String(cur + 1).padStart(2, '0') + '</b> / ' + total;

    var sec = s.getAttribute('data-sec') || '';
    Array.prototype.forEach.call(railBox.children, function (b) {
      b.setAttribute('aria-current', b.dataset.sec === sec ? 'true' : 'false');
    });

    if (history.replaceState) history.replaceState(null, '', '#' + (cur + 1));
    if (hint) hint.style.opacity = cur === 0 ? '1' : '0';
  }

  /* ---------------------------------------------------------- build index */
  function buildIndex() {
    slides.forEach(function (s, i) {
      var b = document.createElement('button');
      b.className = 'thumb' + (s.classList.contains('divider') || s.classList.contains('cover') ? ' is-div' : '');
      b.innerHTML = '<span class="n">' + String(i + 1).padStart(2, '0') + '</span>' +
                    '<span class="t">' + (s.getAttribute('data-title') || '') + '</span>';
      b.addEventListener('click', function () { closeIndex(); go(i); });
      indexWrap.appendChild(b);
    });
  }
  function openIndex()  { indexBox.classList.add('open'); }
  function closeIndex() { indexBox.classList.remove('open'); }
  function toggleIndex(){ indexBox.classList.contains('open') ? closeIndex() : openIndex(); }

  /* --------------------------------------------------------------- rail */
  function buildRail() {
    var seen = {};
    slides.forEach(function (s, i) {
      var sec = s.getAttribute('data-sec');
      var nm  = s.getAttribute('data-secname');
      if (!sec || seen[sec]) return;
      seen[sec] = true;
      var b = document.createElement('button');
      b.dataset.sec = sec;
      b.innerHTML = '<i></i><em>' + sec + ' ' + (nm || '') + '</em>';
      b.addEventListener('click', function () { go(i); });
      railBox.appendChild(b);
    });
  }

  /* ------------------------------------------------------------ controls */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); next(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
    else if (e.key === 'Home') go(0);
    else if (e.key === 'End') go(total - 1);
    else if (e.key.toLowerCase() === 'g') toggleIndex();
    else if (e.key === 'Escape') closeIndex();
    else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }
  });

  var wheelLock = 0;
  window.addEventListener('wheel', function (e) {
    var now = Date.now();
    if (now - wheelLock < 620) return;
    if (Math.abs(e.deltaY) < 14 && Math.abs(e.deltaX) < 14) return;
    wheelLock = now;
    (e.deltaY > 0 || e.deltaX > 0) ? next() : prev();
  }, { passive: true });

  var tx = 0;
  window.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
  window.addEventListener('touchend', function (e) {
    var d = e.changedTouches[0].clientX - tx;
    if (Math.abs(d) > 55) (d < 0 ? next() : prev());
  }, { passive: true });

  document.getElementById('btn-prev').addEventListener('click', prev);
  document.getElementById('btn-next').addEventListener('click', next);
  document.getElementById('btn-index').addEventListener('click', toggleIndex);
  document.getElementById('btn-print').addEventListener('click', function () { window.print(); });
  document.querySelector('#index .close').addEventListener('click', closeIndex);

  // click the stage right/left half to page (ignores links & buttons)
  stage.addEventListener('click', function (e) {
    if (e.target.closest('a,button')) return;
    var r = stage.getBoundingClientRect();
    ((e.clientX - r.left) / r.width > 0.5) ? next() : prev();
  });

  // wake the dock on movement
  var dockT;
  window.addEventListener('mousemove', function () {
    dock.classList.add('awake');
    clearTimeout(dockT);
    dockT = setTimeout(function () { dock.classList.remove('awake'); }, 2200);
  });

  /* ------------------------------------------------------ leader-line prep */
  // give every leader path its own dash length so the trace animation is exact
  document.querySelectorAll('.leader path').forEach(function (p) {
    try { p.style.setProperty('--len', Math.ceil(p.getTotalLength()) + 1); } catch (err) {}
  });

  /* ----------------------------------------------------------------- init */
  buildRail();
  buildIndex();
  fit();

  var start = parseInt((location.hash || '').replace('#', ''), 10);
  cur = (start && start >= 1 && start <= total) ? start - 1 : 0;
  slides[cur].classList.add('is-active', 'in-next');
  sync();
})();
