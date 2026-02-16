(function() {
    function isLoginPage() {
        return /\/admin\/login\/?$/.test(window.location.pathname);
    }

    function init() {
        if (!isLoginPage()) return;

        var bg = document.createElement('div');
        bg.className = 'admin-login-bg';
        var canvas = document.createElement('canvas');
        canvas.id = 'particles-canvas';
        document.body.insertBefore(canvas, document.body.firstChild);
        document.body.insertBefore(bg, document.body.firstChild);

        var ctx = canvas.getContext('2d');
        var particles = [];
        var density = 50;

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }

        function createParticles() {
            particles = [];
            for (var i = 0; i < density; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    radius: Math.random() * 2 + 1,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: (Math.random() - 0.5) * 0.5,
                    opacity: Math.random() * 0.5 + 0.2,
                    color: 'hsl(' + (Math.random() * 60 + 180) + ', 70%, 70%)'
                });
            }
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (var i = 0; i < particles.length; i++) {
                var p = particles[i];
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.shadowBlur = 8;
                ctx.shadowColor = p.color;
                ctx.fillStyle = 'rgba(255, 255, 255, ' + p.opacity + ')';
                ctx.fill();
                p.x += p.vx;
                p.y += p.vy;
                if (p.x <= 0 || p.x >= canvas.width) p.vx *= -1;
                if (p.y <= 0 || p.y >= canvas.height) p.vy *= -1;
            }
            requestAnimationFrame(animate);
        }

        resizeCanvas();
        createParticles();
        animate();

        window.addEventListener('resize', function() {
            resizeCanvas();
            createParticles();
        });

        var h1 = document.querySelector('main h1');
        if (h1) {
            h1.textContent = 'Привет родная :3';
            h1.style.display = '';
        }
        var sub = document.querySelector('main h1 + p');
        if (sub) sub.style.display = 'none';

        var form = document.querySelector('main form') || document.querySelector('form');
        if (form) {
            form.setAttribute('autocomplete', 'off');
            var dummy = document.createElement('div');
            dummy.style.cssText = 'position:absolute;left:-9999px;top:-9999px;width:1px;height:1px;overflow:hidden;';
            var fakeText = document.createElement('input');
            fakeText.type = 'text';
            fakeText.name = 'login_fake';
            fakeText.autocomplete = 'off';
            fakeText.tabIndex = -1;
            var fakePass = document.createElement('input');
            fakePass.type = 'password';
            fakePass.name = 'password_fake';
            fakePass.autocomplete = 'off';
            fakePass.tabIndex = -1;
            dummy.appendChild(fakeText);
            dummy.appendChild(fakePass);
            form.insertBefore(dummy, form.firstChild);
            function clearVisibleInputs() {
                var inputs = form.querySelectorAll('input');
                for (var i = 0; i < inputs.length; i++) {
                    if (inputs[i].name === 'csrfmiddlewaretoken' || inputs[i].type === 'hidden' || inputs[i].name === 'login_fake' || inputs[i].name === 'password_fake') continue;
                    inputs[i].setAttribute('autocomplete', 'off');
                    inputs[i].placeholder = '';
                    inputs[i].value = '';
                    inputs[i].readOnly = true;
                    inputs[i].addEventListener('focus', function fn() {
                        this.readOnly = false;
                        this.removeEventListener('focus', fn);
                    }, true);
                }
            }
            clearVisibleInputs();
            setTimeout(clearVisibleInputs, 150);
            setTimeout(clearVisibleInputs, 400);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
