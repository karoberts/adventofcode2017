using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

namespace cs
{
    class Program
    {
        class Cmd
        {
            public char op;
            public int p1;
            public int p2;
            public char sp1;
            public char sp2;
        }

        static char[] _oldpw = new char[16];

        static void rotright(StringBuilder p, int s)
        {
            s = s % p.Length;
            int np = 0;
            p.CopyTo(0, _oldpw, 0, 16);
            for (int i = p.Length - s; i < p.Length; i++)
                p[np++] = _oldpw[i];
            for (int i = 0; i < p.Length - s; i++)
                p[np++] = _oldpw[i];
              
            /*
            np = ''
            for i in range(len(p) - s, len(p)):
                np += p[i]
            for i in range(0, len(p) - s):
                np += p[i]
                */
        }

        static void swap(StringBuilder p, int ia, int ib)
        {
            int ta = ia;
            ia = Math.Min(ia, ib);
            ib = Math.Max(ta, ib);
            char t = p[ia];
            p[ia] = p[ib];
            p[ib] = t;
        }

        static int find(StringBuilder p, char c)
        {
            for (int i = 0; i < p.Length; i++)
                if (p[i] == c) return i;
            return -1;
        }

        static void run(StringBuilder pw, Cmd[] cmds)
        {
            foreach (var cmd in cmds)
            {
                switch (cmd.op)
                {
                    case 'x': swap(pw, cmd.p1, cmd.p2); break;
                    case 'p': swap(pw, find(pw, cmd.sp1), find(pw, cmd.sp2)); break;
                    case 's': rotright(pw, cmd.p1); break;
                }
            }
        }

        static void Main(string[] args)
        {
            var line = File.ReadAllText("../16.txt");

            //pat = re.compile(r'^([xsp])([a-z]|\d+)(?:/([a-z]|\d+))?$')

            var cmds = new List<Cmd>();
            foreach (var cmd in line.Split(','))
            {
                var m = Regex.Match(cmd, @"^([xsp])([a-z]|\d+)(?:/([a-z]|\d+))?$");
                if (m.Groups[1].Value == "x")
                    cmds.Add(new Cmd { op = 'x', p1 = int.Parse(m.Groups[2].Value), p2 = int.Parse(m.Groups[3].Value) });
                else if (m.Groups[1].Value == "p")
                    cmds.Add(new Cmd { op = 'p', sp1 = m.Groups[2].Value[0], sp2 = m.Groups[3].Value[0] });
                else if (m.Groups[1].Value == "s")
                    cmds.Add(new Cmd { op = 's', p1 = int.Parse(m.Groups[2].Value) });
            }

            var pw = new StringBuilder("abcdefghijklmnop");
            var cmdsA = cmds.ToArray();

            var seen = new Dictionary<string, int>();
            seen.Add(pw.ToString(), 0);
            for (int i = 999999961; i <= 1_000_000_000; i++)
            {
                run(pw, cmdsA);
                var s = pw.ToString();
                if (seen.TryGetValue(s, out int idx))
                    Console.WriteLine($"Saw {s} at {idx} and {i}");
                //else
                    //seen.Add(s, i);
            }
            Console.WriteLine(pw);
        }
    }
}
